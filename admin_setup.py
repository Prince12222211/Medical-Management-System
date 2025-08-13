#!/usr/bin/env python3
"""
Admin Setup Script for Medical Management System
This script helps you create or reset admin credentials for the Django admin panel.
"""

import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(project_dir))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_management.settings')

def setup_admin():
    """Set up admin access for the medical management system"""
    
    try:
        # Initialize Django
        django.setup()
        print("🔧 Medical Management System - Admin Setup")
        print("=" * 50)
        
        from django.contrib.auth.models import User
        
        # Check existing users
        print("\n👥 Current Users:")
        users = User.objects.all()
        for user in users:
            status = "🔑 Superuser" if user.is_superuser else "👤 Regular User"
            print(f"  {status}: {user.username} ({user.email})")
        
        print("\n" + "=" * 50)
        print("Choose an option:")
        print("1. Reset password for existing admin user")
        print("2. Create a new superuser")
        print("3. Make an existing user a superuser")
        print("4. Show admin login information")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            # Reset admin password
            try:
                admin_user = User.objects.get(username='admin')
                new_password = input("Enter new password for admin: ").strip()
                if len(new_password) < 8:
                    print("❌ Password should be at least 8 characters long")
                    return False
                
                admin_user.set_password(new_password)
                admin_user.save()
                print("✅ Admin password updated successfully!")
                print(f"📧 Username: admin")
                print(f"🔐 Password: {new_password}")
                
            except User.DoesNotExist:
                print("❌ Admin user not found")
                return False
                
        elif choice == "2":
            # Create new superuser
            username = input("Enter username: ").strip()
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            
            if User.objects.filter(username=username).exists():
                print(f"❌ User '{username}' already exists")
                return False
            
            if len(password) < 8:
                print("❌ Password should be at least 8 characters long")
                return False
            
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"✅ Superuser '{username}' created successfully!")
            print(f"📧 Username: {username}")
            print(f"🔐 Password: {password}")
            
        elif choice == "3":
            # Make existing user superuser
            username = input("Enter username to make superuser: ").strip()
            try:
                user = User.objects.get(username=username)
                user.is_superuser = True
                user.is_staff = True
                user.save()
                print(f"✅ User '{username}' is now a superuser!")
            except User.DoesNotExist:
                print(f"❌ User '{username}' not found")
                return False
                
        elif choice == "4":
            # Show login info
            print("\n🌐 Admin Panel Access Information:")
            print("=" * 50)
            print("Local Development:")
            print("  URL: http://127.0.0.1:8000/admin/")
            print("\nProduction (Render):")
            print("  URL: https://medical-management-system-v8d5.onrender.com/admin/")
            print("\nExisting Superusers:")
            superusers = User.objects.filter(is_superuser=True)
            for user in superusers:
                print(f"  👤 {user.username} ({user.email})")
            print("\n⚠️  If you don't know the password, use option 1 to reset it.")
            return True
            
        else:
            print("❌ Invalid choice")
            return False
            
        print("\n🌐 Admin Panel URLs:")
        print("  Local: http://127.0.0.1:8000/admin/")
        print("  Production: https://medical-management-system-v8d5.onrender.com/admin/")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def quick_reset_admin():
    """Quick function to reset admin password to a default"""
    django.setup()
    from django.contrib.auth.models import User
    
    try:
        admin_user = User.objects.get(username='admin')
        admin_user.set_password('admin123456')  # Default password
        admin_user.save()
        print("✅ Admin password reset to: admin123456")
        print("🔐 Username: admin")
        print("🌐 Local Admin: http://127.0.0.1:8000/admin/")
        print("🌐 Production Admin: https://medical-management-system-v8d5.onrender.com/admin/")
        return True
    except User.DoesNotExist:
        print("❌ Admin user not found")
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'quick':
        quick_reset_admin()
    else:
        setup_admin()
