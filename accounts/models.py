from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
import random
import string
from datetime import timedelta

# Create your models here.
class EmailVerificationOTP(models.Model):
    """Model to store OTP for email verification"""
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    attempts = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Email Verification OTP'
        verbose_name_plural = 'Email Verification OTPs'
    
    def __str__(self):
        return f"{self.email} - {self.otp}"
    
    @classmethod
    def generate_otp(cls, email):
        """Generate a new OTP for the given email"""
        # Delete any existing OTPs for this email
        cls.objects.filter(email=email).delete()
        
        # Generate random OTP
        otp = ''.join(random.choices(string.digits, k=getattr(settings, 'OTP_LENGTH', 6)))
        
        # Create new OTP record
        otp_record = cls.objects.create(email=email, otp=otp)
        return otp_record
    
    def is_valid(self):
        """Check if OTP is still valid (not expired)"""
        expiry_time = self.created_at + timedelta(minutes=getattr(settings, 'OTP_EXPIRY_MINUTES', 10))
        return timezone.now() < expiry_time and not self.is_verified
    
    def verify(self, entered_otp):
        """Verify the entered OTP"""
        self.attempts += 1
        self.save()
        
        if not self.is_valid():
            return False, "OTP has expired. Please request a new one."
        
        if self.attempts > 3:
            return False, "Too many attempts. Please request a new OTP."
        
        if self.otp == entered_otp:
            self.is_verified = True
            self.save()
            return True, "Email verified successfully!"
        
        return False, "Invalid OTP. Please try again."

class UserProfile(models.Model):
    """Extended user profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    
    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - Profile"
