from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={"class": "form-control"}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileEditForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))


class ChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password_new1 = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password_new2 = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={"class": "form-control"}))
