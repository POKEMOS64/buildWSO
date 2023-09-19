from django.urls import path


from person.views import profileFull

app_name = 'persona'

urlpatterns = [
    path('redactor/', profileFull, name='user'),
]
