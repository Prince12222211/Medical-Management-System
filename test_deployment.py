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
    
    print("\n🎉 All deployment tests passed!")
    
except Exception as e:
    print(f"❌ Deployment test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
