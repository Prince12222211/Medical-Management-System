from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from django.utils import timezone

# Create your models here.
class MedicalRecord(models.Model):
    RECORD_TYPE_CHOICES = [
        ('consultation', 'Consultation'),
        ('diagnosis', 'Diagnosis'),
        ('treatment', 'Treatment'),
        ('surgery', 'Surgery'),
        ('lab_result', 'Lab Result'),
        ('imaging', 'Imaging'),
        ('prescription', 'Prescription'),
        ('vaccination', 'Vaccination'),
    ]
    
    # Record Details
    record_id = models.CharField(max_length=20, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='medical_records')
    appointment = models.ForeignKey(
        Appointment, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='medical_records'
    )
    
    # Record Information
    record_type = models.CharField(max_length=20, choices=RECORD_TYPE_CHOICES)
    date_created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # Clinical Information
    symptoms = models.TextField(blank=True, help_text="Patient symptoms")
    diagnosis = models.TextField(blank=True, help_text="Medical diagnosis")
    treatment_plan = models.TextField(blank=True, help_text="Recommended treatment")
    prescribed_medications = models.TextField(blank=True, help_text="Prescribed medications")
    
    # Follow-up
    follow_up_required = models.BooleanField(default=False)
    follow_up_date = models.DateField(null=True, blank=True)
    follow_up_instructions = models.TextField(blank=True)
    
    # System fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_confidential = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Medical Record'
        verbose_name_plural = 'Medical Records'
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.title} ({self.date_created.strftime('%Y-%m-%d')})"

class Prescription(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('expired', 'Expired'),
    ]
    
    # Prescription Details
    prescription_id = models.CharField(max_length=20, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    medical_record = models.ForeignKey(
        MedicalRecord, 
        on_delete=models.CASCADE, 
        related_name='prescriptions'
    )
    
    # Medication Information
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100, help_text="e.g., '500mg'")
    frequency = models.CharField(max_length=100, help_text="e.g., 'Twice daily'")
    duration = models.CharField(max_length=100, help_text="e.g., '7 days'")
    instructions = models.TextField(help_text="Special instructions for taking the medication")
    
    # Prescription Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    prescribed_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateField()
    end_date = models.DateField()
    
    # Refills
    refills_allowed = models.PositiveIntegerField(default=0)
    refills_used = models.PositiveIntegerField(default=0)
    
    # System fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-prescribed_date']
        verbose_name = 'Prescription'
        verbose_name_plural = 'Prescriptions'
    
    def __str__(self):
        return f"{self.medication_name} for {self.patient.full_name}"
    
    @property
    def refills_remaining(self):
        return self.refills_allowed - self.refills_used
    
    @property
    def is_expired(self):
        return self.end_date < timezone.now().date()

class LabResult(models.Model):
    RESULT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    # Lab Result Details
    lab_id = models.CharField(max_length=20, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='lab_results')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='lab_results')
    medical_record = models.ForeignKey(
        MedicalRecord, 
        on_delete=models.CASCADE, 
        related_name='lab_results'
    )
    
    # Test Information
    test_name = models.CharField(max_length=200)
    test_type = models.CharField(max_length=100)
    ordered_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(null=True, blank=True)
    
    # Results
    status = models.CharField(max_length=20, choices=RESULT_STATUS_CHOICES, default='pending')
    results = models.TextField(blank=True, help_text="Lab test results")
    normal_range = models.CharField(max_length=100, blank=True, help_text="Normal range for the test")
    notes = models.TextField(blank=True, help_text="Additional notes from lab technician")
    
    # Files
    result_file = models.FileField(upload_to='lab_results/', blank=True, null=True)
    
    # System fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-ordered_date']
        verbose_name = 'Lab Result'
        verbose_name_plural = 'Lab Results'
    
    def __str__(self):
        return f"{self.test_name} for {self.patient.full_name}"
