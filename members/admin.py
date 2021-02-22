from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StudentUser, Grade


class StudentUserAdmin(UserAdmin):
    """
    Defines the display in the admin page
    """

    ordering = ("email",)

    list_display = ("email", "full_name",
                    "date_joined", "is_admin")
    search_fields = ("email", "full_name",
                     "date_joined", "last_login")

    readonly_fields = ("id", "date_joined", "last_login", "password")

    fieldsets = (
        (None, {'fields': ('email', 'password', 'has_voted')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'has_voted', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(StudentUser, StudentUserAdmin)
admin.site.register(Grade)