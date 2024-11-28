# Generated by Django 4.2.5 on 2023-09-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inducations', '0006_alter_induimport_gv1_data_alter_induimport_gv2_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='induimport',
            name='gv1_data',
            field=models.IntegerField(blank=True, default='', max_length=50, null=True, verbose_name='Показания ГВ_1'),
        ),
        migrations.AlterField(
            model_name='induimport',
            name='gv2_data',
            field=models.IntegerField(blank=True, default='', max_length=50, null=True, verbose_name='Показание ГВ_2'),
        ),
        migrations.AlterField(
            model_name='induimport',
            name='gv3_data',
            field=models.IntegerField(blank=True, default='', max_length=50, null=True, verbose_name='Показания ГВ_3'),
        ),
        migrations.AlterField(
            model_name='induimport',
            name='gv4_data',
            field=models.IntegerField(blank=True, default='', max_length=50, null=True, verbose_name='Показание ГВ_4'),
        ),
        migrations.AlterField(
            model_name='induimport',
            name='hv1_data',
            field=models.IntegerField(blank=True, default='', max_length=50, null=True, verbose_name='Показание ХВ_1'),
        ),
        migrations.AlterField(
            model_name='induimport',
            name='hv2_data',
            field=models.IntegerField(blank=True, default='', max_length=50, null=True, verbose_name='Показание ХВ_2'),
        ),
        migrations.AlterField(
            model_name='induimport',
            name='hv3_data',
            field=models.IntegerField(blank=True, default='', max_length=50, null=True, verbose_name='Показакние ХВ_3'),
        ),
        migrations.AlterField(
            model_name='induimport',
            name='hv_data',
            field=models.IntegerField(blank=True, default='', max_length=50, null=True, verbose_name='Показания ХВ_4'),
        ),
    ]