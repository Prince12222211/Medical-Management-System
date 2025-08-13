#!/usr/bin/env python3
"""
Deployment Test Script for Medical Management System
This script helps identify potential deployment issues
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

try:
    # Initialize Django
    django.setup()
    
    print("✅ Django setup successful!")
    
    # Test imports
    from django.conf import settings
    from medical_management.views import home, dashboard
    from accounts.models import User
    from patients.models import Patient
    from doctors.models import Doctor
    from appointments.models import Appointment
    from medical_records.models import MedicalRecord
    
    print("✅ All model imports successful!")
    
    # Test URL resolution
    from django.urls import reverse, resolve
    
    # Test home URL
    try:
        home_url = reverse('home')
        print(f"✅ Home URL resolved: {home_url}")
    except Exception as e:
        print(f"❌ Home URL resolution failed: {e}")
    
    # Test admin URL
    try:
        admin_url = reverse('admin:index')
        print(f"✅ Admin URL resolved: {admin_url}")
    except Exception as e:
        print(f"❌ Admin URL resolution failed: {e}")
    
    # Test database connection
    from django.db import connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            print("✅ Database connection successful!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
    
    # Check installed apps
    print(f"✅ Installed apps: {len(settings.INSTALLED_APPS)}")
    for app in settings.INSTALLED_APPS:
        if not app.startswith('django.'):
            print(f"  📱 Custom app: {app}")
    
    # Check static files setup
    print(f"✅ Static URL: {settings.STATIC_URL}")
    print(f"✅ Static root: {settings.STATIC_ROOT}")
    
    # Check templates
    template_dirs = [template['DIRS'] for template in settings.TEMPLATES if template['DIRS']]
    print(f"✅ Template directories: {template_dirs}")
    
    # Check deployment-specific settings
    print("\n🔧 Deployment Configuration Check:")
    print(f"  DEBUG: {settings.DEBUG}")
    print(f"  ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    
    # Check for common deployment URLs
    render_urls = [
        'medical-management-system-v8d5.onrender.com',
        'medical-management-system.onrender.com'
    ]
    print(f"\n🌐 ALLOWED_HOSTS Verification for Render:")
    for url in render_urls:
        if url in settings.ALLOWED_HOSTS:
            print(f"  ✅ {url}: Configured")
        else:
            print(f"  ❌ {url}: Missing (will cause Bad Request 400)")
    
    # Check environment variables
    print(f"\n🔐 Environment Variables:")
    env_vars = ['SECRET_KEY', 'DEBUG', 'ALLOWED_HOSTS', 'EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD']
    for var in env_vars:
        value = os.getenv(var)
        if value:
            if var in ['SECRET_KEY', 'EMAIL_HOST_PASSWORD']:
                print(f"  ✅ {var}: Set (hidden)")
            else:
                print(f"  ✅ {var}: {value}")
        else:
            print(f"  ❌ {var}: Not set")
    
    print("\n🎉 All deployment tests passed!")
    print("\n💡 To fix Bad Request 400 error:")
    print("1. Update render.yaml with correct ALLOWED_HOSTS")
    print("2. Set EMAIL_HOST_PASSWORD in Render dashboard")
    print("3. Redeploy the application")
    
except Exception as e:
    print(f"❌ Deployment test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
