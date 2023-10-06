from django.shortcuts import render, HttpResponseRedirect
# Сама магия ТУТ!!
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserProfilePass, UserProfileFormRed, AddLis, MakeStatement
from ls.forms import ProfileUser
from ls.models import LsModels, selaLsList, chLsList, mkdLsList
from inducations.models import InduImport, InduExport, InduExportSela, InduExportCH
from .models import User, fcecountSQL
# / Сама магия ТУТ!!

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib import auth
from django.views.generic.edit import UpdateView
from django.urls import reverse
from qr_code.qrcode.maker import make_qr
from qr_code.qrcode.utils import QRCodeOptions

def profilePers(request):
    profile = User.objects.get(pk=request.user.pk)
    profile_user = User.objects.filter(pk=request.user.pk)
    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES or None, instance=profile)
        for obj in profile_user:
            username = obj.username
            email = obj.email
            first_name = obj.first_name
            phone = obj.phone
            lic = obj.lic
            lic2 = obj.lic2
            lic3 = obj.lic3
            lic4 = obj.lic4
            lic5 = obj.lic5
            lic6 = obj.lic6
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = username
            instance.email = email
            instance.lic = lic
            instance.lic2 = lic2
            instance.lic3 = lic3
            instance.lic4 = lic4
            instance.lic5 = lic5
            instance.lic6 = lic6
            instance.save()

            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=profile)
    context = {"form": form, 'profile_user': profile_user}
    return render(request, 'users/userredactor.html', context)