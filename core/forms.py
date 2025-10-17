from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="ایمیل",
        required=False,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "ایمیل",
            "autocomplete": "email",
            "dir": "rtl",
        })
    )
    first_name = forms.CharField(
        label="نام",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "نام",
            "dir": "rtl",
        })
    )
    last_name = forms.CharField(
        label="نام خانوادگی",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "نام خانوادگی",
            "dir": "rtl",
        })
    )
    # age = forms.IntegerField(
    #     label="سن",
    #     required=False,
    #     widget=forms.NumberInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "سن",
    #         "min": "0",
    #         "dir": "rtl",
    #         "inputmode": "numeric",
    #     })
    # )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name",
                #    "age", 
                   "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "نام کاربری",
                "autocomplete": "username",
                "dir": "rtl",
            }),
            "password1": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "رمز عبور",
                "autocomplete": "new-password",
                "dir": "rtl",
            }),
            "password2": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "تکرار رمز",
                "autocomplete": "new-password",
                "dir": "rtl",
            }),
        }
        labels = {
            "username": "نام کاربری",
            "password1": "رمز عبور",
            "password2": "تکرار رمز",
        }

