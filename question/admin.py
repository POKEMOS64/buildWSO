from django.contrib import admin
from question.models import qestionModel, questionAbonModel
# Register your models here.

admin.site.register(questionAbonModel)
admin.site.register(qestionModel)
