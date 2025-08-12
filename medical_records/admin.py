from django.contrib import admin
from .models import MedicalRecord, Prescription, LabResult

# Register your models here.
@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = (
        'record_id',
        'patient',
        'doctor',
        'title',
        'record_type',
        'date_created',
        'follow_up_required',
        'is_confidential'
    )
    list_filter = (
        'record_type',
        'date_created',
        'follow_up_required',
        'is_confidential',
        'doctor__department'
    )
    search_fields = (
        'record_id',
        'patient__first_name',
        'patient__last_name',
        'title',
        'description',
        'diagnosis'
    )
    readonly_fields = ('record_id', 'created_at', 'updated_at')
    date_hierarchy = 'date_created'
    
    fieldsets = (
        ('Record Information', {
            'fields': (
                'record_id',
                ('patient', 'doctor'),
                'appointment',
                ('record_type', 'date_created'),
                'title',
                'description'
            )
        }),
        ('Clinical Information', {
            'fields': (
                'symptoms',
                'diagnosis',
                'treatment_plan',
                'prescribed_medications'
            )
        }),
        ('Follow-up', {
            'fields': (
                'follow_up_required',
                'follow_up_date',
                'follow_up_instructions'
            )
        }),
        ('System Information', {
            'fields': (
                'is_confidential',
                'created_at',
                'updated_at'
            ),
            'classes': ('collapse',)
        })
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.record_id:
            # Generate record ID automatically
            last_record = MedicalRecord.objects.all().order_by('id').last()
            if last_record:
                last_id = int(last_record.record_id.replace('REC', ''))
                obj.record_id = f'REC{last_id + 1:06d}'
            else:
                obj.record_id = 'REC000001'
        super().save_model(request, obj, form, change)

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = (
        'prescription_id',
        'patient',
        'doctor',
        'medication_name',
        'dosage',
        'status',
        'prescribed_date',
        'refills_remaining'
    )
    list_filter = (
        'status',
        'prescribed_date',
        'start_date',
        'end_date'
    )
    search_fields = (
        'prescription_id',
        'patient__first_name',
        'patient__last_name',
        'medication_name'
    )
    readonly_fields = ('prescription_id', 'created_at', 'updated_at', 'refills_remaining', 'is_expired')
    date_hierarchy = 'prescribed_date'
    
    def save_model(self, request, obj, form, change):
        if not obj.prescription_id:
            # Generate prescription ID automatically
            last_prescription = Prescription.objects.all().order_by('id').last()
            if last_prescription:
                last_id = int(last_prescription.prescription_id.replace('PRE', ''))
                obj.prescription_id = f'PRE{last_id + 1:06d}'
            else:
                obj.prescription_id = 'PRE000001'
        super().save_model(request, obj, form, change)

@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = (
        'lab_id',
        'patient',
        'doctor',
        'test_name',
        'test_type',
        'status',
        'ordered_date',
        'completed_date'
    )
    list_filter = (
        'status',
        'test_type',
        'ordered_date',
        'completed_date'
    )
    search_fields = (
        'lab_id',
        'patient__first_name',
        'patient__last_name',
        'test_name',
        'test_type'
    )
    readonly_fields = ('lab_id', 'created_at', 'updated_at')
    date_hierarchy = 'ordered_date'
    
    def save_model(self, request, obj, form, change):
        if not obj.lab_id:
            # Generate lab ID automatically
            last_lab = LabResult.objects.all().order_by('id').last()
            if last_lab:
                last_id = int(last_lab.lab_id.replace('LAB', ''))
                obj.lab_id = f'LAB{last_id + 1:06d}'
            else:
                obj.lab_id = 'LAB000001'
        super().save_model(request, obj, form, change)
