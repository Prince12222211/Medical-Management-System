from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    ]
    
    TYPE_CHOICES = [
        ('consultation', 'Consultation'),
        ('follow_up', 'Follow-up'),
        ('emergency', 'Emergency'),
        ('surgery', 'Surgery'),
        ('checkup', 'Regular Checkup'),
    ]
    
    # Appointment Details
    appointment_id = models.CharField(max_length=20, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    
    # Scheduling
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    duration_minutes = models.PositiveIntegerField(default=30)
    
    # Appointment Information
    appointment_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    reason = models.TextField(help_text="Reason for the appointment")
    notes = models.TextField(blank=True, help_text="Additional notes")
    
    # Follow-up
    is_follow_up = models.BooleanField(default=False)
    parent_appointment = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='follow_ups'
    )
    
    # System fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, blank=True)  # Who scheduled the appointment
    
    class Meta:
        ordering = ['appointment_date', 'appointment_time']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        unique_together = ['doctor', 'appointment_date', 'appointment_time']
    
    def __str__(self):
        return f"{self.patient.full_name} with {self.doctor.full_name} on {self.appointment_date} at {self.appointment_time}"
    
    def clean(self):
        # Ensure appointment is not in the past
        if self.appointment_date and self.appointment_time:
            appointment_datetime = timezone.make_aware(
                timezone.datetime.combine(self.appointment_date, self.appointment_time)
            )
            if appointment_datetime < timezone.now():
                raise ValidationError("Appointment cannot be scheduled in the past.")
    
    @property
    def appointment_datetime(self):
        return timezone.datetime.combine(self.appointment_date, self.appointment_time)
    
    @property
    def is_past(self):
        return self.appointment_datetime < timezone.now().replace(tzinfo=None)
    
    @property
    def is_today(self):
        return self.appointment_date == timezone.now().date()
