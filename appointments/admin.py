from django.contrib import admin
from .models import Appointment

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'appointment_id',
        'patient',
        'doctor',
        'appointment_date',
        'appointment_time',
        'appointment_type',
        'status',
        'duration_minutes'
    )
    list_filter = (
        'status', 
        'appointment_type', 
        'appointment_date', 
        'doctor__department',
        'is_follow_up'
    )
    search_fields = (
        'appointment_id',
        'patient__first_name',
        'patient__last_name',
        'doctor__first_name',
        'doctor__last_name',
        'reason'
    )
    readonly_fields = ('appointment_id', 'created_at', 'updated_at')
    date_hierarchy = 'appointment_date'
    
    fieldsets = (
        ('Appointment Details', {
            'fields': (
                'appointment_id',
                ('patient', 'doctor'),
                ('appointment_date', 'appointment_time'),
                'duration_minutes'
            )
        }),
        ('Appointment Information', {
            'fields': (
                'appointment_type',
                'status',
                'reason',
                'notes'
            )
        }),
        ('Follow-up Information', {
            'fields': (
                'is_follow_up',
                'parent_appointment'
            ),
            'classes': ('collapse',)
        }),
        ('System Information', {
            'fields': (
                'created_by',
                'created_at',
                'updated_at'
            ),
            'classes': ('collapse',)
        })
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.appointment_id:
            # Generate appointment ID automatically
            last_appointment = Appointment.objects.all().order_by('id').last()
            if last_appointment:
                last_id = int(last_appointment.appointment_id.replace('APT', ''))
                obj.appointment_id = f'APT{last_id + 1:06d}'
            else:
                obj.appointment_id = 'APT000001'
        
        if not obj.created_by:
            obj.created_by = request.user.username
        
        super().save_model(request, obj, form, change)
