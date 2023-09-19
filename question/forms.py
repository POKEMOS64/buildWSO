from django import forms
from captcha.fields import CaptchaField


class questForms(forms.Form):
    questionItself = forms.CharField(label='задать вопрос',
                                     widget=forms.Textarea(attrs={'cols': 20, 'rows': 4, 'placeholder': 'Как передать показания...'}))
    captcha = CaptchaField(label='Введите код ниже')

    class Meta:
        fields = ('questionItself')
