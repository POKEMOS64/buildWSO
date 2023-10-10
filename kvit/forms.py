from typing import Any
from django import forms
from .models import Receipt

class KvitForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name',}), required=False)
    lic = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет1'}), required=False)
    lic2 = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет2'}), required=False)
    lic3 = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет3'}), required=False)
    lic4 = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет4'}), required=False)
    lic5 = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет5'}), required=False)
    lic6 = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет6'}), required=False)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form_first_name'}), required=False)

    class Meta:
        model = Receipt
        fields = ('username', 'email',
                  'lic_def', 'lic', 'lic2', 'lic3', 'lic4', 'lic5', 'lic6')