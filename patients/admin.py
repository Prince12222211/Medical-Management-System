from django.contrib import admin
from .models import Patient

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'patient_id', 
        'first_name', 
        'last_name', 
        'date_of_birth', 
        'gender', 
        'blood_type',
        'phone_number', 
        'email', 
        'is_active'
    )
    list_filter = ('gender', 'blood_type', 'is_active', 'created_at')
    search_fields = (
        'patient_id', 
        'first_name', 
        'last_name', 
        'email', 
        'phone_number'
    )
    readonly_fields = ('patient_id', 'created_at', 'updated_at', 'age')
    
    fieldsets = (
        ('Personal Information', {
            'fields': (
                'patient_id', 
                ('first_name', 'last_name'), 
                ('date_of_birth', 'gender'), 
                'blood_type'
            )
        }),
        ('Contact Information', {
            'fields': (
                ('phone_number', 'email'), 
                'address'
            )
        }),
        ('Emergency Contact', {
            'fields': (
                'emergency_contact_name', 
                'emergency_contact_phone', 
                'emergency_contact_relationship'
            )
        }),
        ('Medical Information', {
            'fields': (
                'allergies', 
                'medical_history', 
                'current_medications'
            )
        }),
        ('System Information', {
            'fields': (
                'is_active', 
                'created_at', 
                'updated_at'
            ),
            'classes': ('collapse',)
        })
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.patient_id:
            # Generate patient ID automatically
            last_patient = Patient.objects.all().order_by('id').last()
            if last_patient:
                last_id = int(last_patient.patient_id.replace('PAT', ''))
                obj.patient_id = f'PAT{last_id + 1:06d}'
            else:
                obj.patient_id = 'PAT000001'
        super().save_model(request, obj, form, change)
