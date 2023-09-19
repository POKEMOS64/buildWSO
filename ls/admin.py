from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import LsModels, selaLsList, chLsList, mkdLsList


@admin.register(LsModels, selaLsList, chLsList, mkdLsList)
class PersonAdmin(ImportExportModelAdmin):
    pass
