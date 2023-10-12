from django.urls import path

from mail.views import Mail, pdfLove

app_name = 'mail'

urlpatterns = [
    path('mail.asp', Mail, name='mail'),
    path('pdf.asp', pdfLove, name='pdf')
]
