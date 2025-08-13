# Django Admin Panel Access Guide
## Medical Management System

### 🔑 Current Admin Credentials

**Username:** `admin`  
**Password:** `admin123456`  
**Email:** `admin@medicalmanagement.com`

### 🌐 Admin Panel URLs

#### Local Development
- **URL:** `http://127.0.0.1:8000/admin/`
- Use this when running the development server locally

#### Production (Render)
- **URL:** `https://medical-management-system-v8d5.onrender.com/admin/`
- Use this for your live deployment

### 👥 All System Users

1. **admin** - 🔑 Superuser (admin@medicalmanagement.com)
2. **Prince2306** - 👤 Regular User (princeverma9504@gmail.com)
3. **Prince5047** - 👤 Regular User (princeverma5047@gmail.com)

### 🚀 How to Access Admin Panel

#### Step 1: Open Admin URL
- For production: Go to `https://medical-management-system-v8d5.onrender.com/admin/`
- For local: Go to `http://127.0.0.1:8000/admin/`

#### Step 2: Enter Login Credentials
```
Username: admin
Password: admin123456
```

#### Step 3: Click "Log in"

### 🛠️ What You Can Do in Admin Panel

Once logged in, you can manage:

1. **👥 Users & Groups**
   - Create/edit user accounts
   - Assign permissions and groups
   - Manage staff and superuser status

2. **🩺 Medical Management Data**
   - **Accounts:** User profiles and OTP records
   - **Patients:** Patient information and records
   - **Doctors:** Doctor profiles and specializations
   - **Appointments:** Appointment scheduling and status
   - **Medical Records:** Patient medical history

3. **🔧 System Administration**
   - View site configuration
   - Check database entries
   - Monitor user activity

### 🔐 Changing Admin Password

#### Method 1: Using the Script
```bash
cd /home/prince-verma/medical_management
source venv/bin/activate
python admin_setup.py
# Choose option 1 to reset admin password
```

#### Method 2: Through Django Shell
```bash
cd /home/prince-verma/medical_management
source venv/bin/activate
python manage.py shell
```

Then in the shell:
```python
from django.contrib.auth.models import User
admin = User.objects.get(username='admin')
admin.set_password('your_new_password')
admin.save()
```

#### Method 3: Through Admin Panel
1. Login to admin panel
2. Click on "Users" 
3. Click on "admin" user
4. Scroll down to password section
5. Click "this form" link next to password
6. Enter new password twice
7. Save

### 🆕 Creating New Admin Users

#### Using the Script:
```bash
python admin_setup.py
# Choose option 2 to create new superuser
```

#### Using Django Command:
```bash
python manage.py createsuperuser
```

### 🔍 Troubleshooting

#### Problem: "Invalid username or password"
**Solutions:**
1. Verify you're using: username=`admin`, password=`admin123456`
2. Check if you're on the correct URL
3. Reset password using the admin_setup.py script

#### Problem: "You don't have permission to access admin"
**Solutions:**
1. Make sure the user is marked as "staff" and "superuser"
2. Use the admin_setup.py script option 3 to grant superuser privileges

#### Problem: Can't access production admin panel
**Solutions:**
1. Ensure your Render deployment is working (no 400 errors)
2. Check that the admin URLs are properly configured
3. Verify the deployment includes all migrations

### 📱 Admin Panel Mobile Access

The Django admin panel is responsive and can be accessed from mobile devices using the same URLs and credentials.

### ⚠️ Security Recommendations

1. **Change the default password immediately** after first login
2. **Use a strong password** (at least 12 characters)
3. **Limit admin access** to trusted users only
4. **Regular password rotation** for production systems
5. **Enable two-factor authentication** if available

### 🆘 Emergency Admin Reset

If you're completely locked out, run:
```bash
cd /home/prince-verma/medical_management
source venv/bin/activate
python admin_setup.py quick
```

This will reset admin password to `admin123456`

---

**Last Updated:** August 13, 2025  
**Admin Password Set:** `admin123456`  
**Production URL:** https://medical-management-system-v8d5.onrender.com/admin/
