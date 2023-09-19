from django.contrib import admin


# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import InduExport, InduImport, InduExportCH, InduExportSela


@admin.register(InduImport, InduExport, InduExportCH, InduExportSela)
class InducationsAdmin(ImportExportModelAdmin):
    pass
