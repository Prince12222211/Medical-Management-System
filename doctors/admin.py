from django.contrib import admin
from .models import Doctor, Department

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_department', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'doctor_id', 
        'first_name', 
        'last_name', 
        'specialization', 
        'department', 
        'license_number',
        'phone_number', 
        'is_active'
    )
    list_filter = ('department', 'specialization', 'gender', 'is_active', 'created_at')
    search_fields = (
        'doctor_id', 
        'first_name', 
        'last_name', 
        'license_number',
        'email', 
        'phone_number'
    )
    readonly_fields = ('doctor_id', 'created_at', 'updated_at', 'age')
    
    fieldsets = (
        ('User Account', {
            'fields': ('user',)
        }),
        ('Personal Information', {
            'fields': (
                'doctor_id', 
                ('first_name', 'last_name'), 
                ('date_of_birth', 'gender')
            )
        }),
        ('Professional Information', {
            'fields': (
                ('license_number', 'specialization'), 
                'department',
                'years_of_experience',
                'education'
            )
        }),
        ('Contact Information', {
            'fields': (
                ('phone_number', 'email'), 
                'office_address'
            )
        }),
        ('Schedule & Fees', {
            'fields': (
                'consultation_fee',
                'available_days',
                'available_hours'
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
        if not obj.doctor_id:
            # Generate doctor ID automatically
            last_doctor = Doctor.objects.all().order_by('id').last()
            if last_doctor:
                last_id = int(last_doctor.doctor_id.replace('DOC', ''))
                obj.doctor_id = f'DOC{last_id + 1:06d}'
            else:
                obj.doctor_id = 'DOC000001'
        super().save_model(request, obj, form, change)
