#!/usr/bin/env python3
"""
🧪 Medical Management System - Complete System Test
===================================================

This script performs comprehensive testing of the Medical Management System
including Gmail OTP email functionality.
"""

import os
import sys
import time
import requests
from datetime import datetime

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_management.settings')

try:
    import django
    django.setup()
    from django.contrib.auth.models import User
    from django.core.mail import send_mail
    from django.conf import settings
    from accounts.models import EmailVerificationOTP
    print("✅ Django modules imported successfully")
except Exception as e:
    print(f"❌ Error importing Django modules: {e}")
    sys.exit(1)

def test_server_response():
    """Test if the Django server is responding"""
    try:
        print("\n🌐 TESTING SERVER RESPONSE")
        print("-" * 40)
        
        # Test homepage
        response = requests.get('http://localhost:8000/', timeout=10)
        if response.status_code == 200:
            print("✅ Homepage: Server responding (200 OK)")
        else:
            print(f"⚠️  Homepage: Unexpected status code {response.status_code}")
        
        # Test signup page
        response = requests.get('http://localhost:8000/accounts/signup/', timeout=10)
        if response.status_code == 200:
            print("✅ Signup page: Accessible (200 OK)")
        else:
            print(f"⚠️  Signup page: Unexpected status code {response.status_code}")
            
        # Test static files
        response = requests.get('http://localhost:8000/static/css/medical-style.css', timeout=10)
        if response.status_code == 200:
            print("✅ Static CSS: Loading correctly")
        else:
            print(f"⚠️  Static CSS: Status code {response.status_code}")
            
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ Server not running! Start with: python3 manage.py runserver 0.0.0.0:8000")
        return False
    except Exception as e:
        print(f"❌ Server test error: {e}")
        return False

def test_gmail_configuration():
    """Test Gmail SMTP configuration"""
    print("\n📧 TESTING GMAIL CONFIGURATION")
    print("-" * 40)
    
    # Check environment variables
    email_host_user = getattr(settings, 'EMAIL_HOST_USER', None)
    email_host_password = getattr(settings, 'EMAIL_HOST_PASSWORD', None)
    
    if email_host_user:
        print(f"✅ Gmail address configured: {email_host_user}")
    else:
        print("❌ EMAIL_HOST_USER not configured")
        return False
        
    if email_host_password:
        print("✅ Gmail app password configured: ****** (hidden)")
    else:
        print("❌ EMAIL_HOST_PASSWORD not configured")
        return False
        
    # Check other email settings
    print(f"✅ Email host: {settings.EMAIL_HOST}")
    print(f"✅ Email port: {settings.EMAIL_PORT}")
    print(f"✅ Use TLS: {settings.EMAIL_USE_TLS}")
    
    return True

def test_send_otp_email():
    """Test sending OTP email"""
    print("\n📬 TESTING OTP EMAIL SENDING")
    print("-" * 40)
    
    try:
        # Generate a test OTP
        test_otp = "123456"
        test_email = settings.EMAIL_HOST_USER
        test_first_name = "Test User"
        
        subject = "Email Verification - Medical Management System"
        message = f"""Dear {test_first_name},

Thank you for registering with Medical Management System!

Your email verification OTP is: {test_otp}

This OTP is valid for 10 minutes.

Please enter this OTP on the verification page to complete your registration.

If you didn't create this account, please ignore this email.

Best regards,
Medical Management System Team"""
        
        print(f"📧 Sending test OTP email to: {test_email}")
        print(f"🔢 Test OTP: {test_otp}")
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[test_email],
            fail_silently=False
        )
        
        print("✅ OTP email sent successfully!")
        print("📱 Check your Gmail inbox for the test OTP email")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send OTP email: {e}")
        return False

def test_database_models():
    """Test database models"""
    print("\n🗄️  TESTING DATABASE MODELS")
    print("-" * 40)
    
    try:
        # Test User model
        user_count = User.objects.count()
        print(f"✅ User model accessible: {user_count} users in database")
        
        # Test OTP model
        otp_count = EmailVerificationOTP.objects.count()
        print(f"✅ EmailVerificationOTP model accessible: {otp_count} OTP records in database")
        
        return True
        
    except Exception as e:
        print(f"❌ Database model error: {e}")
        return False

def display_system_info():
    """Display system information"""
    print("\n🏥 MEDICAL MANAGEMENT SYSTEM STATUS")
    print("=" * 50)
    print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 Python Version: {sys.version.split()[0]}")
    print(f"🎯 Django Version: {django.get_version()}")
    print(f"📁 Project Directory: {os.getcwd()}")
    print(f"🌐 Server URL: http://localhost:8000/")
    print(f"📧 Gmail SMTP: {settings.EMAIL_HOST_USER}")

def display_test_results(results):
    """Display final test results"""
    print("\n🧪 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    total_tests = len(results)
    passed_tests = sum(results.values())
    
    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\n📊 Overall: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! System is ready for use.")
        print("\n🚀 Next Steps:")
        print("1. Visit http://localhost:8000/ to access the homepage")
        print("2. Try creating a new account - OTP emails will be sent to Gmail!")
        print("3. Test the complete signup → OTP verification → login flow")
    else:
        print("⚠️  Some tests failed. Please review the issues above.")

def main():
    """Run all tests"""
    display_system_info()
    
    # Run tests
    results = {
        "Server Response": test_server_response(),
        "Gmail Configuration": test_gmail_configuration(),
        "OTP Email Sending": test_send_otp_email(),
        "Database Models": test_database_models()
    }
    
    display_test_results(results)
    
    # Additional instructions
    print("\n📖 USAGE INSTRUCTIONS")
    print("=" * 50)
    print("1. 🏠 Homepage: http://localhost:8000/")
    print("2. 📝 Signup: http://localhost:8000/accounts/signup/")
    print("3. 🔐 Login: http://localhost:8000/accounts/login/")
    print("4. 📊 Dashboard: http://localhost:8000/dashboard/ (after login)")
    print("\n📧 When you signup:")
    print("   → OTP email will be sent to your Gmail inbox")
    print("   → Enter the 6-digit OTP to verify your account")
    print("   → Complete registration and access the dashboard")

if __name__ == "__main__":
    main()
