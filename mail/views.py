from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def Mail(request):
    send_mail('MUP "Balakovo-VODOKANAL"', 'Send on is WSO-Project',
              settings.EMAIL_HOST_USER, ['it@bal-vod.ru'])
    return render(request, 'mail/send.html')
