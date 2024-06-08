from django import forms
from django.contrib import admin

from accounts.models import User, RegisterUserOtp


@admin.register(User)
class UserRegister(admin.ModelAdmin):
    list_display = ("phone", "fullname", "is_admin")


@admin.register(RegisterUserOtp)
class RegisterUserOtp(admin.ModelAdmin):
    list_display = ("phone", "code", "data_exprition")
