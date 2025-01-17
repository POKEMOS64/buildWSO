from django.db import models
from datetime import datetime
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class indxpages(models.Model):
    title = models.CharField(verbose_name='Название страницы', max_length=200)
    pagesText = RichTextUploadingField(verbose_name="Содержимое страницы")

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Другие разделы"
        verbose_name_plural = 'Другие'

class IndexPost(models.Model):
    title = models.CharField(verbose_name='Название страницы', max_length=200)
    pagesText = RichTextUploadingField(verbose_name="Содержимое страницы")
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('informations:post', kwargs={'post_id': self.pk})

    class Meta():
        verbose_name = "Страницы"
        verbose_name_plural = 'Страницы'

class WaterModel(models.Model):
    title = models.CharField(verbose_name='Название страницы', max_length=200)
    pagesText = RichTextUploadingField(verbose_name="Содержимое страницы")

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Раздел"
        verbose_name_plural = 'Разделы'


class WaterModelDoc(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    fileTypes = models.FileField(upload_to='waterdoc/%Y/%m/%d')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Документы по воде"
        verbose_name_plural = 'Водоснабжение Приложение'


class WaterModelDocDisposal(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    fileTypes = models.FileField(upload_to='waterdoc/%Y/%m/%d')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Документы по воде"
        verbose_name_plural = 'Водоотведени Приложение'

# Информация


class InfoModelDoc(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    fileTypes = models.FileField(upload_to='info/%Y/%m/%d')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "2023"
        verbose_name_plural = 'за 2023'


class InfoModelDocLast(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    fileTypes = models.FileField(upload_to='info/2022/')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "2022"
        verbose_name_plural = 'за 2022'


class InfoModelDocbeforeLast(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    fileTypes = models.FileField(upload_to='info/2021/')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "2021"
        verbose_name_plural = 'за 2021'


class InfoModelDocnazLast(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    fileTypes = models.FileField(upload_to='info/2020/')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "2020"
        verbose_name_plural = 'за 2020'
