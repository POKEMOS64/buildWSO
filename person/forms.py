from typing import Any
from django import forms
from django.contrib.auth.forms import UserChangeForm

from users.models import User


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваше имя'}), required=False)
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваше имя'}), required=False)
    lic = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваше имя'}), required=False)
    lic2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваше имя'}), required=False)
    lic3 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваше имя'}), required=False)
    lic4 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваше имя'}), required=False)
    lic5 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваше имя'}), required=False)
    lic6 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваше имя'}), required=False)
    lic_def = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Выбранный лицевой'}), required=False)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form_first_name'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'phone',
                  'lic_def', 'lic', 'lic2', 'lic3', 'lic4', 'lic5', 'lic6')
