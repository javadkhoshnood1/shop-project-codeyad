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

        for user in User.objects.all():
            if phone == user.phone:
                raise ValidationError("این کاربر درون سایت وجود دارد")

        if len(phone) > 11 or len(phone) < 11:
            raise ValidationError("شماره تماس باید 11 رقم باشد. ")
        return phone


class UserVerificationCodeForm(forms.Form):
    code = forms.CharField(validators=[validators.MaxLengthValidator(4)], label=" کد تایید ")


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("phone", "fullname", "password")

    widgets = {
        'password': forms.TextInput(attrs={'name': 'password'}), }


class EditProfileUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "name": "password1"}),
                                label="رمز عبور جدید")
    password2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "name": "password2"}),
                                label=" تکرار رمز عبور جدید")

    class Meta:
        model = User
        fields = ["phone", "fullname", "password", "email", "discription", "image"]

    widgets = {
        'password': forms.TextInput(attrs={'name': 'password'}),
        'email': forms.TextInput(attrs={'name': 'email'}),
        'discription': forms.TextInput(attrs={'name': 'discription'}),
        "image": forms.FileInput(attrs={"name": "image"})

    }

    def __init__(self, *args, **kwargs):
        super(EditProfileUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
