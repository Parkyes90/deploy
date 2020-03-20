from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as __

from .models import User


class CustomUserAdmin(UserAdmin):
    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (__("Personal Info"), {"fields": ("name",)}),
        (
            __("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser")},
        ),
        (__("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
