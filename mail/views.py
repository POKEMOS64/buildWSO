from django.shortcuts import render
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from kvit.models import Receipt
import reportlab
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
import tempfile
# Create your views here.

def pdfLove(request):

    return render(request, 'mail/pdf.html')

def GenKvit(val,lic):
    p = canvas.Canvas(val + lic +'.pdf')
    p.drawString(100,500,"Тест PDF")
    p.showPage()
    p.save()

def Mail(request):
    assem = Receipt.objects.all()
    ListTuple = []
    LicList = []
    for i in assem:
        userX = i.user_name
        MailX = i.email_pole
        LicList = [i.lic1_pole,
                   i.lic2_pole,
                   i.lic3_pole,
                   i.lic4_pole,
                   i.lic5_pole,
                   i.lic6_pole
                   ]
        ListTrue = [
            i.lic11_pole,
            i.lic12_pole,
            i.lic13_pole,
            i.lic14_pole,
            i.lic15_pole,
            i.lic16_pole
        ]
        print(LicList)
        ListTuple.append(MailX)
    datatuple = len(ListTuple)
    i = 0
    
    while i < datatuple:
        for x in range(6):
            ListTuple__ = ListTuple[i]
            path = str('kvitres/' + MailX)
            if True == ListTrue[x]:
                LicList__ = "Электронная квитанция Лицевой счет:" + str(LicList[x])
                print(True)
                GenKvit(path,str(LicList[x]))
                email = EmailMessage(
                    LicList__,
                    'Электронная квитанция за октябрь',
                    settings.DEFAULT_FROM_EMAIL,
                    [ListTuple__],
                    reply_to= ['bot@bal-vod.ru'],
                    headers={'Message': 'test'}
                )
                email.attach_file(path + str(LicList[x]) + '.pdf')
                email.send()
                
        i += 1
    return render(request, 'mail/send.html')
