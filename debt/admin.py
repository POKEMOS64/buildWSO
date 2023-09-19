from django.contrib import admin
from .models import debtCHModel, debtURModel, tamponingModel
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(debtURModel, debtCHModel, tamponingModel)
class debtAdmin(ImportExportModelAdmin):
    pass
