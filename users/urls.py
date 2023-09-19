from django.urls import path

from users.views import login, registration, profile, passwordreset, profilePers, profileAddLis

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('user/', profile, name='profile'),
    path('password/', passwordreset, name='password'),
    path('profilepersona/', profilePers, name='rdt'),
    path('addlis/', profileAddLis, name='addlis'),


]
