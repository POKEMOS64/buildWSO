from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Receipt
from .forms import KvitForm
from users.models import User
# Create your views here.

def Kvit(request):
    listkvit = Receipt.objects.all()
    profile = User.objects.get(pk=request.user.pk)
    list_prof = Receipt.objects.filter(user_name = profile)
    profile_user = User.objects.filter(pk=request.user.pk)
    form = KvitForm()
    if request.method == 'POST':
        form = KvitForm(data = request.POST)
        if form.is_valid():
            for x in profile_user:
                userX = x.username
                emailX = x.email
                licX = x.lic
                lic2X = x.lic2
                lic3X = x.lic3
                lic4X = x.lic4
                lic5X = x.lic5
                lic6X = x.lic6
            feed = Receipt(
                user_name = userX,
                email_pole = emailX,
                lic1_pole = licX,
                lic2_pole = lic2X,
                lic3_pole = lic3X,
                lic4_pole = lic4X,
                lic5_pole = lic5X,
                lic6_pole = lic6X,
                lic11_pole = form.cleaned_data['lic'],
                lic12_pole = form.cleaned_data['lic2'],
                lic13_pole = form.cleaned_data['lic3'],
                lic14_pole = form.cleaned_data['lic4'],
                lic15_pole = form.cleaned_data['lic5'],
                lic16_pole = form.cleaned_data['lic6'],
            )
            if list_prof:
                Receipt.objects.filter(user_name = userX).update(
                    lic11_pole = form.cleaned_data['lic'],
                    lic12_pole = form.cleaned_data['lic2'],
                    lic13_pole = form.cleaned_data['lic3'],
                    lic14_pole = form.cleaned_data['lic4'],
                    lic15_pole = form.cleaned_data['lic5'],
                    lic16_pole = form.cleaned_data['lic6'],
                )
            else:
                feed.save()
                return HttpResponseRedirect(reverse('kvit:index'))

    else:
        form = KvitForm()
    context={
        'form':form,
        'listkvit':listkvit,
    }
    return render(request, 'kvit/index.html', context )