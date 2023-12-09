from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

## stop at 1:11:01


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your username",
                "class": "w-full px-6 py-4 rounded-xl",
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Your email address",
                "class": "w-full px-6 py-4 rounded-xl",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Your password",
                "class": "w-full px-6 py-4 rounded-xl",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repeat password",
                "class": "w-full px-6 py-4 rounded-xl",
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Check if passwords match
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Passwords do not match. Please enter the same password in both fields"
            )

        return cleaned_data
