from django.contrib import admin
from .models import WaterModel, WaterModelDoc,WaterModelDocDisposal, InfoModelDoc, InfoModelDocLast, InfoModelDocbeforeLast, InfoModelDocnazLast, indxpages, IndexPost
# Register your models here.
admin.site.register(indxpages)
admin.site.register(WaterModel)
admin.site.register(WaterModelDoc)
admin.site.register(WaterModelDocDisposal)
admin.site.register(InfoModelDoc)
admin.site.register(InfoModelDocLast)
admin.site.register(InfoModelDocbeforeLast)
admin.site.register(InfoModelDocnazLast)
admin.site.register(IndexPost)
