from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserPol, userPers, fcecountSQL
from django.db import models

# Register your models here.


admin.site.register(UserAdmin)
admin.site.register(UserPol)
admin.site.register(userPers)
# admin.site.register(fcecountSQL)
