from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import advert, advertText


@admin.register(advert, advertText)
class AdvertAdmin(ImportExportModelAdmin):
    pass
