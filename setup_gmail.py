#!/usr/bin/env python3
"""
Gmail Setup Script for Medical Management System
This script helps you configure Gmail SMTP for sending OTP emails.
"""

import os
import getpass
import subprocess
import sys

def print_header():
    print("=" * 60)
    print("🏥 MEDICAL MANAGEMENT SYSTEM - GMAIL SETUP")
    print("=" * 60)
    print()

def print_step(step_num, title):
    print(f"\n📌 STEP {step_num}: {title}")
    print("-" * 40)

def check_2fa_status():
    print_step(1, "CHECK 2-FACTOR AUTHENTICATION STATUS")
    print("First, you need to check if 2-Factor Authentication is enabled on your Gmail account.")
    print()
    print("🔗 Go to: https://myaccount.google.com/security")
    print()
    print("Look for '2-Step Verification' and ensure it's turned ON.")
    
    while True:
        response = input("\nIs 2-Factor Authentication enabled on your Gmail? (y/n): ").lower()
        if response in ['y', 'yes']:
            break
        elif response in ['n', 'no']:
            print("\n❌ You MUST enable 2-Factor Authentication first!")
            print("📝 Instructions:")
            print("1. Go to https://myaccount.google.com/security")
            print("2. Click on '2-Step Verification'")
            print("3. Follow the setup process")
            print("4. Come back here once it's enabled")
            sys.exit(1)
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def get_app_password():
    print_step(2, "GENERATE GMAIL APP PASSWORD")
    print("You need to generate an App Password for the Medical Management System.")
    print()
    print("🔗 Go to: https://myaccount.google.com/apppasswords")
    print()
    print("📝 Instructions:")
    print("1. Click 'Select app' and choose 'Mail'")
    print("2. Click 'Select device' and choose 'Other (Custom name)'")
    print("3. Type: Medical Management System")
    print("4. Click 'Generate'")
    print("5. Copy the 16-character password (it will look like: abcd efgh ijkl mnop)")
    print()
    
    while True:
        app_password = getpass.getpass("Enter your 16-character Gmail App Password: ").strip()
        
        # Remove spaces if user copied with spaces
        app_password_clean = app_password.replace(' ', '')
        
        if len(app_password_clean) == 16 and app_password_clean.isalnum():
            return app_password_clean
        else:
            print("❌ Invalid App Password format.")
            print("The App Password should be 16 characters (letters and numbers).")
            print("Example: abcdefghijklmnop")

def create_env_file(email, app_password):
    print_step(3, "CREATE CONFIGURATION FILE")
    
    env_content = f"""# Gmail Configuration for Medical Management System
# Generated automatically - DO NOT SHARE THIS FILE!

# Your Gmail address
EMAIL_HOST_USER={email}

# Your Gmail App Password (16 characters)
EMAIL_HOST_PASSWORD={app_password}
"""
    
    env_path = '.env'
    
    with open(env_path, 'w') as f:
        f.write(env_content)
    
    # Secure the file
    os.chmod(env_path, 0o600)
    
    print(f"✅ Configuration saved to {env_path}")
    print("🔒 File permissions set to secure mode (600)")

def test_email_config():
    print_step(4, "TEST EMAIL CONFIGURATION")
    print("Testing if the email configuration works...")
    
    try:
        # Test Django email backend
        os.environ['DJANGO_SETTINGS_MODULE'] = 'medical_management.settings'
        
        import django
        django.setup()
        
        from django.core.mail import send_mail
        from django.conf import settings
        
        print(f"📧 Sending test email from: {settings.EMAIL_HOST_USER}")
        
        send_mail(
            'Medical Management System - Email Test',
            'Congratulations! Your Gmail SMTP configuration is working correctly.\n\nYou can now receive OTP emails in your Gmail inbox.\n\n🏥 Medical Management System',
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        
        print("✅ Test email sent successfully!")
        print("📬 Check your Gmail inbox for the test email.")
        
    except Exception as e:
        print(f"❌ Email test failed: {str(e)}")
        print("Please check your App Password and try again.")
        return False
    
    return True

def update_gitignore():
    """Add .env to .gitignore to prevent committing secrets"""
    gitignore_path = '.gitignore'
    env_entry = '.env\n'
    
    try:
        # Read existing .gitignore
        if os.path.exists(gitignore_path):
            with open(gitignore_path, 'r') as f:
                content = f.read()
            
            if '.env' not in content:
                with open(gitignore_path, 'a') as f:
                    f.write('\n# Environment variables\n.env\n')
                print("✅ Added .env to .gitignore")
            else:
                print("✅ .env already in .gitignore")
        else:
            with open(gitignore_path, 'w') as f:
                f.write('# Environment variables\n.env\n')
            print("✅ Created .gitignore with .env entry")
    except Exception as e:
        print(f"⚠️  Could not update .gitignore: {e}")

def main():
    print_header()
    
    print("This script will help you configure Gmail SMTP for sending OTP emails.")
    print("You'll need your Gmail account and will generate an App Password.")
    print()
    
    # Get email address
    email = input("Enter your Gmail address (princeverma9504@gmail.com): ").strip()
    if not email:
        email = "princeverma9504@gmail.com"
    
    # Validate email format
    if not email.endswith('@gmail.com'):
        print("❌ Please enter a valid Gmail address.")
        sys.exit(1)
    
    print(f"Using Gmail: {email}")
    
    # Check 2FA status
    check_2fa_status()
    
    # Get App Password
    app_password = get_app_password()
    
    # Create .env file
    create_env_file(email, app_password)
    
    # Update .gitignore
    update_gitignore()
    
    # Test configuration
    if test_email_config():
        print("\n🎉 SUCCESS! Gmail SMTP is now configured.")
        print("\n📋 Next steps:")
        print("1. Start the Django server: python3 manage.py runserver")
        print("2. Try creating a new account - OTP emails will be sent to Gmail!")
        print("3. Check your Gmail inbox (and spam folder) for OTP emails")
    else:
        print("\n❌ Setup completed but email test failed.")
        print("You may need to check your App Password and try again.")
    
    print("\n" + "=" * 60)
    print("🔒 SECURITY REMINDER:")
    print("- Never share your App Password")
    print("- The .env file contains sensitive information")
    print("- .env is added to .gitignore to prevent accidental commits")
    print("=" * 60)

if __name__ == "__main__":
    main()
