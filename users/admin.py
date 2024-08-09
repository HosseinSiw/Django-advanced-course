from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    list_display = ("email", "name", "is_active", "is_staff", "is_superuser",)
    search_fields = ("email", "name", "is_active", "is_staff", "is_superuser",)
    list_filter = ("is_active", "is_staff", "is_superuser", "is_verified")
    ordering = ("email",)

    # Adding fields specification
    fieldsets = (
        ("Personal", {"fields": ("name", "email",)}),
        ("Perms", {"fields": ("is_active", "is_staff", "is_superuser", "is_verified")}),
        ("Dates", {"fields": ('last_login',)}),
    )
    # Editing fields specification
    add_fieldsets = (
        ("Personal", {"fields": ("name", "email", "password1", "password2")}),
        ("Perms", {"fields": ("is_active", "is_staff", "is_superuser", "is_verified")}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
