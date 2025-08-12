from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.utils import timezone
from datetime import date, timedelta

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from medical_records.models import MedicalRecord


def home(request):
    """Home page view"""
    return render(request, 'home.html')


@login_required
def dashboard(request):
    """Main dashboard view with statistics"""
    today = timezone.now().date()
    
    # Get basic statistics
    total_patients = Patient.objects.filter(is_active=True).count()
    total_doctors = Doctor.objects.filter(is_active=True).count()
    
    # Today's appointments
    todays_appointments = Appointment.objects.filter(
        appointment_date=today
    ).order_by('appointment_time')
    
    # Recent appointments (last 7 days)
    week_ago = today - timedelta(days=7)
    recent_appointments = Appointment.objects.filter(
        appointment_date__gte=week_ago,
        appointment_date__lte=today
    ).order_by('-appointment_date', '-appointment_time')[:10]
    
    # Appointment statistics
    pending_appointments = Appointment.objects.filter(
        status='scheduled',
        appointment_date__gte=today
    ).count()
    
    completed_appointments = Appointment.objects.filter(
        status='completed',
        appointment_date=today
    ).count()
    
    # Recent medical records
    recent_records = MedicalRecord.objects.filter(
        date_created__gte=week_ago
    ).order_by('-date_created')[:5]
    
    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'todays_appointments': todays_appointments,
        'recent_appointments': recent_appointments,
        'pending_appointments': pending_appointments,
        'completed_appointments': completed_appointments,
        'recent_records': recent_records,
        'today': today,
    }
    
    return render(request, 'dashboard.html', context)


@login_required
def patients_list(request):
    """List all patients"""
    patients = Patient.objects.filter(is_active=True).order_by('last_name', 'first_name')
    return render(request, 'patients/list.html', {'patients': patients})


@login_required
def doctors_list(request):
    """List all doctors"""
    doctors = Doctor.objects.filter(is_active=True).order_by('last_name', 'first_name')
    return render(request, 'doctors/list.html', {'doctors': doctors})


@login_required
def appointments_list(request):
    """List all appointments"""
    appointments = Appointment.objects.all().order_by('-appointment_date', '-appointment_time')
    return render(request, 'appointments/list.html', {'appointments': appointments})
