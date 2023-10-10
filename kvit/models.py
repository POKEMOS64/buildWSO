from django.db import models

# Create your models here.

class Receipt(models.Model):
    user_name = models.CharField(max_length=248, verbose_name='Пользователь')
    email_pole = models.EmailField(max_length=248, verbose_name='Почта')
    lic1_pole = models.IntegerField(max_length=50, verbose_name='Лицевой №1', blank=True, null=True)
    lic2_pole = models.IntegerField(max_length=50, verbose_name='Лицевой №2', blank=True, null=True)
    lic3_pole = models.IntegerField(max_length=50, verbose_name='Лицевой №3', blank=True, null=True)
    lic4_pole = models.IntegerField(max_length=50, verbose_name='Лицевой №4', blank=True, null=True)
    lic5_pole = models.IntegerField(max_length=50, verbose_name='Лицевой №5', blank=True, null=True)
    lic6_pole = models.IntegerField(max_length=50, verbose_name='Лицевой №6', blank=True, null=True)
    lic11_pole = models.BooleanField(verbose_name='Лицевой №1-Доп поле', blank=True, null=True)
    lic12_pole = models.BooleanField(verbose_name='Лицевой №2-Доп поле', blank=True, null=True)
    lic13_pole = models.BooleanField(verbose_name='Лицевой №3-Доп поле', blank=True, null=True)
    lic14_pole = models.BooleanField(verbose_name='Лицевой №4-Доп поле', blank=True, null=True)
    lic15_pole = models.BooleanField(verbose_name='Лицевой №5-Доп поле', blank=True, null=True)
    lic16_pole = models.BooleanField(verbose_name='Лицевой №6-Доп поле', blank=True, null=True)

    def __str__(self):
        return str(self.user_name)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'