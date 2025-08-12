# 📧 Gmail SMTP Setup for Medical Management System

This guide will help you configure Gmail SMTP to send OTP emails directly to your Gmail inbox instead of displaying them in the terminal.

## 🚀 Quick Setup (Automated)

Run the automated setup script:

```bash
python3 setup_gmail.py
```

The script will guide you through all steps automatically!

## 📋 Manual Setup Instructions

### Step 1: Enable 2-Factor Authentication

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Look for **"2-Step Verification"**
3. If it's not enabled, click to enable it
4. Follow the setup process (you can use SMS, authenticator app, etc.)

### Step 2: Generate Gmail App Password

1. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
2. Click **"Select app"** → Choose **"Mail"**
3. Click **"Select device"** → Choose **"Other (Custom name)"**
4. Type: **"Medical Management System"**
5. Click **"Generate"**
6. Copy the 16-character password (format: `abcd efgh ijkl mnop`)

⚠️ **Important**: This is NOT your regular Gmail password!

### Step 3: Create Environment File

Create a file named `.env` in your project directory:

```bash
# Gmail Configuration for Medical Management System
EMAIL_HOST_USER=princeverma9504@gmail.com
EMAIL_HOST_PASSWORD=your-16-character-app-password-here
```

Replace `your-16-character-app-password-here` with the actual App Password from Step 2.

### Step 4: Secure the Environment File

```bash
chmod 600 .env
```

### Step 5: Update .gitignore

Add `.env` to your `.gitignore` file to prevent committing secrets:

```bash
echo ".env" >> .gitignore
```

## 🧪 Testing the Configuration

Test if email sending works:

```bash
python3 -c "
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'medical_management.settings'
import django
django.setup()
from django.core.mail import send_mail
from django.conf import settings
send_mail('Test', 'Gmail SMTP is working!', settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER])
print('✅ Test email sent successfully!')
"
```

## 🎯 How It Works

1. **Signup Process**: User creates account → OTP generated → Email sent to Gmail
2. **Email Delivery**: Django uses Gmail SMTP → Sends professional OTP email
3. **User Experience**: User receives OTP in Gmail inbox → Verifies account

## 📬 Email Template

The OTP emails will look like this:

```
Subject: Email Verification - Medical Management System

Dear [First Name],

Thank you for registering with Medical Management System!

Your email verification OTP is: 123456

This OTP is valid for 10 minutes.

Please enter this OTP on the verification page to complete your registration.

If you didn't create this account, please ignore this email.

Best regards,
Medical Management System Team
```

## 🔧 Troubleshooting

### "Authentication failed" Error
- Double-check your App Password (16 characters)
- Ensure 2-Factor Authentication is enabled
- Make sure you're using the App Password, not your regular password

### "Connection refused" Error
- Check your internet connection
- Verify Gmail SMTP settings (smtp.gmail.com:587)

### Email goes to Spam
- Check your spam folder
- Gmail may initially mark emails as spam until the sending pattern is established

### App Password Generation Issues
- Ensure 2-Factor Authentication is fully enabled
- Try refreshing the App Passwords page
- Generate a new App Password if the old one doesn't work

## 🔐 Security Notes

- **Never share your App Password**
- The `.env` file contains sensitive information
- App Passwords bypass 2-Factor Authentication for the specific app
- You can revoke App Passwords anytime from your Google Account
- The `.env` file should never be committed to version control

## 📱 Mobile Testing

You can also test on mobile by:
1. Starting the server: `python3 manage.py runserver 0.0.0.0:8000`
2. Finding your IP address: `ip addr show`
3. Accessing from mobile: `http://your-ip:8000`

## 🎉 Success!

Once configured, your Medical Management System will send professional OTP emails directly to Gmail inboxes, providing a seamless user experience for account verification!
