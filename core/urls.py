"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from dispatch.views import dispatchViews
from question.views import questViews
from informations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('persona/', include('person.urls', namespace='persona')),
    path('ls/', include('ls.urls', namespace='ls')),
    path('advertisement/', include('advertisement.urls', namespace='advertisement')),
    path('dispatch/', dispatchViews, name='pages'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('abon/debt/', include('debt.urls', namespace='debt')),
    path('question/', include('question.urls', namespace='question')),
    path('captcha/', include('captcha.urls')),
    path('', include('abon.urls', namespace='abon')),
    path('info/', include('informations.urls', namespace='informations')),
    path('mail/', include('mail.urls', namespace='mail')),
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
