from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import UserProfile, EmailVerificationOTP

class CustomUserCreationForm(UserCreationForm):
    """Custom signup form with additional fields"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your phone number'
        })
    )
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Enter your address'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create a password'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists.")
        return username
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = False  # User will be activated after email verification
        
        if commit:
            user.save()
            
            # Create user profile
            UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data.get('phone_number', ''),
                date_of_birth=self.cleaned_data.get('date_of_birth'),
                address=self.cleaned_data.get('address', ''),
                is_email_verified=False
            )
        
        return user

class OTPVerificationForm(forms.Form):
    """Form for OTP verification"""
    otp = forms.CharField(
        max_length=6,
        min_length=6,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control text-center',
            'placeholder': '000000',
            'maxlength': '6',
            'style': 'font-size: 1.5rem; letter-spacing: 0.5rem;'
        }),
        help_text='Enter the 6-digit OTP sent to your email'
    )
    
    def __init__(self, email=None, *args, **kwargs):
        self.email = email
        super().__init__(*args, **kwargs)
    
    def clean_otp(self):
        otp = self.cleaned_data.get('otp')
        if not otp.isdigit():
            raise ValidationError("OTP must contain only digits.")
        return otp
    
    def verify_otp(self):
        """Verify the OTP"""
        if not self.is_valid():
            return False, "Invalid form data"
        
        otp = self.cleaned_data['otp']
        
        try:
            otp_record = EmailVerificationOTP.objects.filter(
                email=self.email,
                is_verified=False
            ).latest('created_at')
            
            return otp_record.verify(otp)
        except EmailVerificationOTP.DoesNotExist:
            return False, "No valid OTP found. Please request a new one."

class ResendOTPForm(forms.Form):
    """Form for resending OTP"""
    email = forms.EmailField(widget=forms.HiddenInput())
    
    def __init__(self, email=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if email:
            self.fields['email'].initial = email
