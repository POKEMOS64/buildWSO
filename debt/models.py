from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class debtCHModel(models.Model):
    namber = models.PositiveIntegerField(
        max_length=50, verbose_name='№ п/п', null=True, blank=True)
    personalAccount = models.PositiveIntegerField(
        max_length=50, verbose_name="№ л. счета", null=True, blank=True)
    residentialAdress = models.CharField(
        max_length=50, verbose_name="Адрес должника", null=True, blank=True)
    debt = models.CharField(
        max_length=50, verbose_name="Долг", null=True, blank=True)

    def __str__(self):
        return f"{float(self.personalAccount)}"

    def __str__(self):
        return str(self.residentialAdress)

    def __str__(self):
        return str(self.debt)

    def __str__(self):
        return str(self.namber)

    class Meta:
        verbose_name = 'Должник'
        verbose_name_plural = 'Должники'


class debtURModel(models.Model):
    namber = models.PositiveIntegerField(
        max_length=50, verbose_name='№ п/п', null=True, blank=True)
    personalAccount = models.PositiveIntegerField(
        max_length=50, verbose_name="№ л. счета", null=True, blank=True)
    personalName = models.CharField(
        max_length=50, verbose_name="Название", null=True, blank=True)
    residentialAdress = models.CharField(
        max_length=50, verbose_name="Адрес должника", null=True, blank=True)
    debt = models.CharField(
        max_length=50, verbose_name="Долг", null=True, blank=True)

    def __str__(self):
        return f"{float(self.personalAccount)}"

    def __str__(self):
        return str(self.personalName)

    def __str__(self):
        return str(self.residentialAdress)

    def __str__(self):
        return str(self.debt)

    def __str__(self):
        return str(self.namber)

    class Meta:
        verbose_name = 'Должник'
        verbose_name_plural = 'Должники Упр.'


class tamponingModel(models.Model):
    namber = models.PositiveIntegerField(
        max_length=50, verbose_name='№ п/п', null=True, blank=True)
    personalAccount = models.PositiveIntegerField(
        max_length=50, verbose_name="№ л. счета", null=True, blank=True)
    residentialAdress = models.CharField(
        max_length=50, verbose_name="Адрес должника", null=True, blank=True)
    debt = models.CharField(
        max_length=50, verbose_name="Долг", null=True, blank=True)

    def __str__(self):
        return f"{float(self.personalAccount)}"

    def __str__(self):
        return str(self.residentialAdress)

    def __str__(self):
        return str(self.debt)

    def __str__(self):
        return str(self.namber)

    class Meta:
        verbose_name = 'Должник'
        verbose_name_plural = 'Должники на тампонирование'
