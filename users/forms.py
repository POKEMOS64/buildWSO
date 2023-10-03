from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User, UserPol


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_username', 'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form_pass', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Логин'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваше имя'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваша фамилия'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваша электронный адрес'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Придумайте пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')

# Не используется-------------------------------------------------------------


class UserPol(forms.Form):
    user_pk = forms.CharField(max_length=200, required=False)
    user_name = forms.CharField(max_length=200, required=False)

    class Meta:
        fields = ('user_pk', 'user_name')
# /Не используется-------------------------------------------------------------


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваше имя'}), required=False)
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваш телефон'}), required=False)
    lic = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет'}), required=False)
    lic2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет'}), required=False)
    lic3 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет'}), required=False)
    lic4 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет'}), required=False)
    lic5 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет'}), required=False)
    lic6 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Лицевой счет'}), required=False)
    lic_def = forms.CharField(
        widget=forms.HiddenInput(
            attrs={'class': 'form_first_name',
                   'placeholder': 'Выбранный лицевой'}
        ),
        required=False)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form_first_name'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'phone',
                  'lic_def', 'lic', 'lic2', 'lic3', 'lic4', 'lic5', 'lic6')


# Не используется-------------------------------------------------------------
class UserProfileFormRed(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Ваше имя'}), required=False)
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'placeholder': 'Телефон'}), required=False)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form_first_name'}), required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'phone')
# /Не используется-------------------------------------------------------------


class UserProfilePass(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    password = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class AddLis(forms.Form):
    fac_lis = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=True)
    summ_ = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=True)

    class Meta:
        fields = ('fac_lis', 'summ_')


# id_ls;name_dom;name_kv;codsch_hv1;hv1_data;codsh_gv1;gv1_data;codsch_hv2;hv2_data;codsch_gv2;gv2_data;codsch_hv3;hv3_data;codsch_gv3;gv3_data;codsch_hv4;hv_data;codsh_gv4;gv4_data


class MakeStatement(forms.Form):
    id_ls = forms.CharField(label='Номер лицевого счета', widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)

    name_dom = forms.CharField(label='Номер дома', widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    name_kv = forms.CharField(label='Номер квартиры', widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    codsch_hv1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    hv1_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    codsh_gv1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    gv1_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    codsch_hv2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    hv2_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    codsch_gv2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    gv2_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    codsch_hv3 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    hv3_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    codsch_gv3 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    gv3_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    codsch_hv4 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    hv_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    codsh_gv4 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)
    gv4_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', }), required=False)

    class Meta:
        fields = ('id_ls', 'name_dom', 'codsch_hv1', 'hv1_data', 'gv1_data', 'codsch_hv2', 'hv2_data', 'codsch_gv2',
                  'gv2_data', 'codsch_hv3', 'hv3_data', 'codsch_gv3', 'gv3_data', 'codsch_hv4', 'hv_data', 'codsh_gv4', 'gv4_data')
