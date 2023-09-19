from django.contrib import admin

from .models import dispatchText, dispatch
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(dispatch, dispatchText)
class dispatchAdmin(ImportExportModelAdmin):
    pass
