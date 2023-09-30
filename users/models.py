from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(
        max_length=50, verbose_name='Телефон', null='True', blank=True)
    lic = models.CharField(
        max_length=50, verbose_name='Лицевой основной', null='True', blank=True)
    lic2 = models.CharField(
        max_length=50, verbose_name='Дополнительный лицевой №2', null='True', blank=True)
    lic3 = models.CharField(
        max_length=50, verbose_name='Дополнительный лицевой №3', null='True', blank=True)
    lic4 = models.CharField(
        max_length=50, verbose_name='Дополнительный лицевой №4', null='True', blank=True)
    lic5 = models.CharField(
        max_length=50, verbose_name='Дополнительный лицевой №5', null='True', blank=True)
    lic6 = models.CharField(
        max_length=50, verbose_name='Дополнительный лицевой №6', null='True', blank=True)
    lic_def = models.CharField(
        max_length=50, verbose_name='Выбранный лицевой', null='True', blank=True)

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class userPers(models.Model):
    licIdx = models.CharField(max_length=100)
    userP = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.userP

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Привязки'


class UserPol(models.Model):
    user_pk = models.CharField(max_length=50, verbose_name='ID')
    user_name = models.CharField(max_length=50, verbose_name='Пользователь')
    s_m = models.CharField(max_length=50, verbose_name='Лицевой тест1')
    s_mX = models.CharField(max_length=50, verbose_name='Лицевой тест2')
    s_mXL = models.CharField(max_length=50, verbose_name='Лицевой тест3')
    s_mXXL = models.CharField(max_length=50, verbose_name='Лицевой тест4')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Данные'
        verbose_name_plural = 'Данные'


class fcecountSQL(models.Model):
    FCNUMBERCOUNT = models.CharField(
        max_length=200, verbose_name='Лицевой счет')
    MAX = models.DateField(verbose_name="Дата платежа",
                           null='True', blank=True)
    MAX1 = models.CharField(verbose_name='Сумма')

    def __str__(self):
        return self.FCNUMBERCOUNT

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Реестр платежей'
