from django.contrib import admin
from .models import WaterModel, WaterModelDoc, InfoModelDoc, InfoModelDocLast, InfoModelDocbeforeLast, InfoModelDocnazLast
# Register your models here.

admin.site.register(WaterModel)
admin.site.register(WaterModelDoc)
admin.site.register(InfoModelDoc)
admin.site.register(InfoModelDocLast)
admin.site.register(InfoModelDocbeforeLast)
admin.site.register(InfoModelDocnazLast)
