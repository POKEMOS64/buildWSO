from django.urls import path

from .views import Kvit, KvitResult

app_name='kvit'

urlpatterns=[
    path('forma.asp', Kvit , name='forma'),
    path('idx.asp', KvitResult , name='index'),
]