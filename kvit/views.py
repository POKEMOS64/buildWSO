from django.shortcuts import render
from .models import Receipt
from .forms import KvitForm
from users.models import User
# Create your views here.

def Kvit(request):
    listkvit = Receipt.objects.get(pk = request.user_name.pk)
    profile = User.objects.get(pk=request.user.pk)
    profile_user = User.objects.filter(pk=request.user.pk)
    form = KvitForm()
    if request.method == 'POST':
        form = KvitForm(data = request.POST)
        if form.is_valid():
            for i in profile_user:
                user_name = i.username
                email_pole = i.email
                



    else:
        form = KvitForm()
    context={

    }
    return render(request, 'kvit/index.html', context )