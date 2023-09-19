from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.contrib import auth
from users.models import User
from person.forms import UserProfileForm
from django.contrib import messages


def profileFull(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user,
                               data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('persona:user'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {"form": form}
    return render(request, 'users/userredactor.html', context)
