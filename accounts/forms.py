from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from accounts.models import User


def start_phone_0(value):
    if value[0] != "0":
        raise forms.ValidationError("شماره تماس باید بای صفر آغاز و 11 رقم باشد")


class UserLoginForm(forms.Form):
    phone = forms.CharField(label="شماره تماس", widget=forms.TextInput(attrs={"class": ""}),
                            validators=[start_phone_0])
    password = forms.CharField(widget=forms.TextInput(attrs={"class": ""}), label="رمز عبور")

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        if len(phone) > 11 or len(phone) < 11:
            raise ValidationError("شماره تماس باید 11 رقم باشد. ")
        return phone


class UserRegisterForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": ""}), label="شماره تماس", validators=[start_phone_0])

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        if len(phone) > 11 or len(phone) < 11:
            raise ValidationError("شماره تماس باید 11 رقم باشد. ")
        return phone


class UserVerificationCodeForm(forms.Form):
    code = forms.CharField(validators=[validators.MaxLengthValidator(4)], label=" کد تایید ")


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("phone", "fullname", "password")
