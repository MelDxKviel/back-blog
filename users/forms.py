from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileEditForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.EmailField()


class ChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    password_new1 = forms.CharField(max_length=65, widget=forms.PasswordInput)
    password_new2 = forms.CharField(max_length=65, widget=forms.PasswordInput)
