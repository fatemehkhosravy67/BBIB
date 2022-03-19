from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'branch_code']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('branch_code',)}),
    )  # this will allow to change these fields in admin module


admin.site.register(CustomUser, CustomUserAdmin)
