from django.contrib import admin
from .models import EmailVerificationOTP, UserProfile

# Register your models here.
@admin.register(EmailVerificationOTP)
class EmailVerificationOTPAdmin(admin.ModelAdmin):
    list_display = ('email', 'otp', 'created_at', 'is_verified', 'attempts')
    list_filter = ('is_verified', 'created_at')
    search_fields = ('email',)
    readonly_fields = ('otp', 'created_at')
    ordering = ('-created_at',)
    
    def has_add_permission(self, request):
        return False  # Prevent manual creation

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'is_email_verified', 'created_at')
    list_filter = ('is_email_verified', 'created_at')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'address')
        }),
        ('Personal Information', {
            'fields': ('date_of_birth',)
        }),
        ('Verification Status', {
            'fields': ('is_email_verified',)
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
