from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import LsModels, selaLsList, chLsList, mkdLsList
from users.models import fcecountSQL


@admin.register(LsModels, selaLsList, chLsList, mkdLsList, fcecountSQL)
class PersonAdmin(ImportExportModelAdmin):
    pass
