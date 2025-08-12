from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from .forms import CustomUserCreationForm, OTPVerificationForm, ResendOTPForm
from .models import EmailVerificationOTP, UserProfile

def signup_view(request):
    """User signup view"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Generate and send OTP
            otp_record = EmailVerificationOTP.generate_otp(user.email)
            send_otp_email(user.email, otp_record.otp, user.first_name)
            
            messages.success(request, 
                f'Account created successfully! An OTP has been sent to {user.email}. '
                f'Please verify your email to complete registration.')
            
            return redirect('accounts:verify_otp', email=user.email)
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def verify_otp_view(request, email=None):
    """OTP verification view"""
    if not email:
        messages.error(request, 'Email not provided.')
        return redirect('accounts:signup')
    
    # Check if user exists
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error(request, 'Invalid email address.')
        return redirect('accounts:signup')
    
    # Check if already verified
    if user.is_active:
        messages.info(request, 'Your account is already verified.')
        return redirect('login')
    
    if request.method == 'POST':
        form = OTPVerificationForm(email=email, data=request.POST)
        if form.is_valid():
            success, message = form.verify_otp()
            
            if success:
                # Activate user account
                user.is_active = True
                user.save()
                
                # Update user profile
                profile, created = UserProfile.objects.get_or_create(user=user)
                profile.is_email_verified = True
                profile.save()
                
                messages.success(request, message + ' You can now login to your account.')
                return redirect('login')
            else:
                messages.error(request, message)
    else:
        form = OTPVerificationForm(email=email)
    
    # Get OTP info for display
    try:
        otp_record = EmailVerificationOTP.objects.filter(
            email=email,
            is_verified=False
        ).latest('created_at')
        otp_created_at = otp_record.created_at
        attempts_left = max(0, 3 - otp_record.attempts)
    except EmailVerificationOTP.DoesNotExist:
        otp_created_at = None
        attempts_left = 0
    
    context = {
        'form': form,
        'email': email,
        'otp_created_at': otp_created_at,
        'attempts_left': attempts_left,
        'otp_expiry_minutes': getattr(settings, 'OTP_EXPIRY_MINUTES', 10),
        'resend_form': ResendOTPForm(email=email)
    }
    
    return render(request, 'accounts/verify_otp.html', context)

def resend_otp_view(request):
    """Resend OTP view"""
    if request.method == 'POST':
        form = ResendOTPForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            try:
                user = User.objects.get(email=email)
                if user.is_active:
                    messages.info(request, 'Your account is already verified.')
                    return redirect('login')
                
                # Generate new OTP
                otp_record = EmailVerificationOTP.generate_otp(email)
                send_otp_email(email, otp_record.otp, user.first_name)
                
                messages.success(request, f'A new OTP has been sent to {email}')
                return redirect('accounts:verify_otp', email=email)
            
            except User.DoesNotExist:
                messages.error(request, 'Invalid email address.')
                return redirect('accounts:signup')
    
    messages.error(request, 'Invalid request.')
    return redirect('accounts:signup')

def send_otp_email(email, otp, first_name):
    """Send OTP email to user"""
    subject = 'Email Verification - Medical Management System'
    message = f'''
Dear {first_name},

Thank you for registering with Medical Management System!

Your email verification OTP is: {otp}

This OTP is valid for {getattr(settings, 'OTP_EXPIRY_MINUTES', 10)} minutes.

Please enter this OTP on the verification page to complete your registration.

If you didn't create this account, please ignore this email.

Best regards,
Medical Management System Team
'''
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        print(f"OTP email sent to {email}: {otp}")  # For development
    except Exception as e:
        print(f"Failed to send email to {email}: {str(e)}")
        # In production, you might want to log this error
