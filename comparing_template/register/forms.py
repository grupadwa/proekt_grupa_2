from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []
