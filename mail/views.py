from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def Mail(request):
    send_mail('МУП "Балаково-Водоканал"', 'Тут будет квитанция',
              settings.EMAIL_HOST_USER, ['srv@bal-vod.ru'])
    return render(request, 'mail/send.html')
