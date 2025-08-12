from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    head_of_department = models.ForeignKey(
        'Doctor', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='headed_department'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    # Link to Django User model for authentication
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Personal Information
    doctor_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    # Professional Information
    license_number = models.CharField(max_length=50, unique=True)
    specialization = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    years_of_experience = models.PositiveIntegerField()
    education = models.TextField(help_text="Educational background and qualifications")
    
    # Contact Information
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField()
    office_address = models.TextField()
    
    # Schedule Information
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    available_days = models.CharField(
        max_length=100, 
        help_text="e.g., 'Monday, Tuesday, Wednesday, Friday'"
    )
    available_hours = models.CharField(
        max_length=50, 
        help_text="e.g., '9:00 AM - 5:00 PM'"
    )
    
    # System fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"
    
    @property
    def full_name(self):
        return f"Dr. {self.first_name} {self.last_name}"
    
    @property
    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
