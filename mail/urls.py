from django.urls import path

from mail.views import Mail

app_name = 'mail'

urlpatterns = [
    path('mail', Mail, name='mail')
]
