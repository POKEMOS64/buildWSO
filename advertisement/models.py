from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class advert(models.Model):

    dataAd = models.DateField(max_length=50, verbose_name='Дата')
    gapTime = models.CharField(
        max_length=50, verbose_name='Промежуток времени Не использовать',null=True, blank=True)
    gapTimeUp = models.DateTimeField(
        max_length=50, verbose_name='Промежуток времени Начало',null=True, blank=True)
    gapTimeDown = models.DateTimeField(
        max_length=50, verbose_name='Промежуток времени Конец',null=True, blank=True)
    optMaps = models.CharField(
        max_length=100, verbose_name='Улица или поселок с номером', null=True, blank=True)
    optMaps_one = models.CharField(
        max_length=100, verbose_name='Улица или поселок с номером', null=True, blank=True)
    optMaps_two = models.CharField(
        max_length=100, verbose_name='Улица или поселок с номером', null=True, blank=True)
    optMaps_three = models.CharField(
        max_length=100, verbose_name='Улица или поселок с номером', null=True, blank=True)
    optMaps_four = models.CharField(
        max_length=100, verbose_name='Улица или поселок с номером', null=True, blank=True)
    optMaps_five = models.CharField(
        max_length=100, verbose_name='Улица или поселок с номером', null=True, blank=True)
    optMaps_six = models.CharField(
        max_length=100, verbose_name='Улица или поселок с номером', null=True, blank=True)
    optMaps_seven = models.CharField(
        max_length=100, verbose_name='Улица или поселок с номером', null=True, blank=True)

    def __str__(self):
        return self.optMaps

    class Meta:
        verbose_name = 'Обход по домам'
        verbose_name_plural = 'Обход по домам'


class advertText(models.Model):
    header = RichTextUploadingField(verbose_name="заголовок")
    sectionText = RichTextUploadingField(verbose_name="Содержимое")

    def __str__(self):
        self.objName = 'Содержимое страницы'
        return self.objName

    class Meta:
        verbose_name = 'Содержимое страницы'
        verbose_name_plural = 'Содержимое страниц'
