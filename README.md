# 🏥 Medical Management System

A comprehensive Django-based Medical Management System designed for healthcare practices, clinics, and hospitals. This system provides complete patient management, appointment scheduling, medical records, and user account management with advanced email verification.

## 🚀 Features

### 📋 Core Modules
- **👥 Patient Management** - Complete patient registration, profiles, and records
- **👨‍⚕️ Doctor Management** - Doctor profiles, specializations, and availability 
- **📅 Appointment System** - Smart scheduling with conflict detection
- **📄 Medical Records** - Secure patient medical history and documentation
- **🔐 Account Management** - User registration with OTP email verification

### ✨ Advanced Features
- **📧 Gmail SMTP Integration** - Professional OTP email delivery
- **🎨 Modern Responsive Design** - Bootstrap-based UI with animations
- **🔒 Secure Authentication** - Email verification with OTP validation
- **⏱️ Real-time Validations** - Instant form validation and feedback
- **📱 Mobile-Friendly** - Responsive design for all devices
- **🛡️ Admin Dashboard** - Comprehensive Django admin integration

## 🛠️ Technology Stack

### Backend
- **Django 4.2+** - Python web framework
- **SQLite** - Database (easily configurable for PostgreSQL/MySQL)
- **Django ORM** - Database abstraction layer

### Frontend
- **HTML5/CSS3** - Modern markup and styling
- **Bootstrap 5** - Responsive CSS framework
- **JavaScript (ES6+)** - Interactive functionality
- **Custom CSS Animations** - Enhanced user experience

### Email System
- **Gmail SMTP** - Professional email delivery
- **OTP Verification** - 6-digit email verification codes
- **Auto-expiry** - 10-minute OTP validity with security features

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git
- Gmail account with 2-Factor Authentication

### Quick Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/medical-management-system.git
   cd medical-management-system
   ```

2. **Install Dependencies**
   ```bash
   pip install django python-dotenv requests
   ```

3. **Database Setup**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser
   ```

4. **Gmail SMTP Configuration**
   ```bash
   python3 setup_gmail.py
   ```
   Follow the interactive setup to configure Gmail SMTP.

5. **Run the Development Server**
   ```bash
   python3 manage.py runserver 0.0.0.0:8000
   ```

6. **Access the Application**
   - Homepage: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/
   - Signup: http://localhost:8000/accounts/signup/

## 🔧 Configuration

### Gmail SMTP Setup

The system requires Gmail SMTP for sending OTP emails:

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate App Password**:
   - Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
   - Create password for "Medical Management System"
3. **Run Setup Script**: `python3 setup_gmail.py`

### Environment Variables

Create a `.env` file with:
```bash
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-16-character-app-password
```

## 🗂️ Project Structure

```
medical_management/
├── 📁 accounts/           # User authentication & OTP verification
│   ├── models.py          # EmailVerificationOTP, UserProfile
│   ├── views.py           # Signup, login, OTP verification
│   ├── urls.py            # Authentication routes
│   └── templates/         # Auth templates
├── 📁 patients/           # Patient management
│   ├── models.py          # Patient model
│   ├── views.py           # Patient CRUD operations
│   └── templates/         # Patient templates
├── 📁 doctors/            # Doctor management
│   ├── models.py          # Doctor model with specializations
│   ├── views.py           # Doctor management views
│   └── templates/         # Doctor templates
├── 📁 appointments/       # Appointment scheduling
│   ├── models.py          # Appointment model
│   ├── views.py           # Scheduling logic
│   └── templates/         # Appointment templates
├── 📁 medical_records/    # Medical records management
│   ├── models.py          # MedicalRecord model
│   ├── views.py           # Records management
│   └── templates/         # Records templates
├── 📁 static/             # Static assets
│   ├── css/               # Custom styles with animations
│   ├── js/                # JavaScript functionality
│   └── images/            # Logo and images
├── 📁 templates/          # Global templates
├── 📄 manage.py           # Django management script
├── 📄 settings.py         # Django configuration
├── 📄 setup_gmail.py      # Gmail SMTP setup utility
├── 📄 test_system.py      # System testing script
└── 📄 requirements.txt    # Python dependencies
```

## 🎯 Usage

### For Healthcare Staff

1. **Patient Registration**
   - Navigate to Patients section
   - Add new patient with complete details
   - Upload medical documents

2. **Doctor Management**
   - Add doctors with specializations
   - Set availability schedules
   - Manage doctor profiles

3. **Appointment Scheduling**
   - Book appointments with conflict detection
   - View appointment calendar
   - Manage appointment status

4. **Medical Records**
   - Create and update patient records
   - Track medical history
   - Generate reports

### For New Users

1. **Account Creation**
   - Visit signup page
   - Fill registration form
   - Receive OTP via Gmail
   - Verify email with 6-digit OTP
   - Access dashboard

## 🧪 Testing

Run the comprehensive system test:
```bash
python3 test_system.py
```

This tests:
- Server response
- Gmail SMTP configuration  
- OTP email delivery
- Database connectivity
- All system components

## 📱 Mobile Support

The application is fully responsive and supports:
- **Smartphones** - iOS and Android
- **Tablets** - iPad and Android tablets  
- **Desktop** - All modern browsers
- **Network Access** - Run on `0.0.0.0:8000` for LAN access

## 🔐 Security Features

- **Email Verification** - OTP-based account verification
- **Session Management** - Secure Django sessions
- **CSRF Protection** - Built-in Django CSRF middleware
- **Password Security** - Django's built-in password validation
- **Environment Variables** - Sensitive data protection
- **OTP Expiry** - Time-limited verification codes
- **Rate Limiting** - Prevents brute force attempts

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Requirements

### System Requirements
- **Python**: 3.8 or higher
- **Django**: 4.2 or higher
- **RAM**: Minimum 1GB (2GB recommended)
- **Storage**: 100MB for application + database size
- **Internet**: Required for Gmail SMTP

### Python Dependencies
```
Django>=4.2.0
python-dotenv>=1.0.0
requests>=2.28.0
```

## 🐛 Troubleshooting

### Common Issues

**Gmail SMTP Authentication Failed**
- Ensure 2-Factor Authentication is enabled
- Use App Password, not regular password
- Check `.env` file configuration

**Server Won't Start**
- Check if port 8000 is available
- Run migrations: `python3 manage.py migrate`
- Check for syntax errors in code

**OTP Emails Not Received**
- Check Gmail spam folder
- Verify Gmail SMTP settings
- Run email test: `python3 test_system.py`

**Static Files Not Loading**
- Run: `python3 manage.py collectstatic`
- Check `STATIC_URL` in settings.py
- Verify file permissions

## 📞 Support

For support and questions:
- 📧 Create an issue on GitHub
- 📚 Check the documentation
- 🔧 Run the system test for diagnostics

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Django Community** - For the amazing framework
- **Bootstrap Team** - For the responsive design framework
- **Gmail SMTP** - For reliable email delivery
- **Python Community** - For excellent ecosystem

## 📈 Version History

- **v1.0.0** - Initial release with core features
  - Patient, Doctor, Appointment management
  - Medical Records system
  - User authentication with OTP
  - Gmail SMTP integration
  - Responsive UI with animations

---

**⭐ If you find this project helpful, please give it a star!**

Built with ❤️ using Django, Bootstrap, and modern web technologies.
# Medical-Management-System
