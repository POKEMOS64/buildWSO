from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class qestionModel(models.Model):
    department = [
        (1, 'Ответили'),
        (2, 'Повторение'),
        (3, 'Отдел ПТО'),
        (4, 'Отдел закупок'),
    ]
    dataTimes = models.DateField(default=datetime.now, null=True, blank=True)

    questionItself = models.TextField(verbose_name='Ваш вопрос')
    departmentReplied = models.PositiveSmallIntegerField(
        choices=department, verbose_name='Отдел', null=True, blank=True)
    answerToTheQuestion = RichTextUploadingField(
        verbose_name='Ответ', null=True, blank=True)

    def __str__(self):
        otvet = 'Не ответили'
        if self.departmentReplied == 1:
            otvet = 'Ответил'
        if self.departmentReplied == 2:
            otvet = 'Повторение'
        self.y = 'Дата: ' + str(self.dataTimes) + '  |  ' + \
            self.questionItself + '  |  Статус :   ' + otvet
        return f"{self.y}"

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопрос всем'


class questionAbonModel(models.Model):
    numberIsSet = models.CharField(
        max_length=200, verbose_name="Имя автора", null=True, blank=True)
    dataTimes = models.DateField(default=datetime.now)
    questionItself = models.TextField(verbose_name='Ваш вопрос')
    answerToTheQuestion = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return f"{self.dataTimes}"

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = "Вопросы абоненскому"
