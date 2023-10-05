from django.db import models

# ID_LS;NAME_DOM;NAME_KV;CODSCH_HV1;HV1;CODSCH_GV1;GV1;CODSCH_HV2;HV2;CODSCH_GV2;GV2;CODSCH_HV3;HV3;CODSCH_GV3;GV3;CODSCH_HV4;HV4;CODSCH_GV4;GV4

# id_ls;name_dom;name_kv;codsch_hv1;hv1_data;codsh_gv1;gv1_data;codsch_hv2;hv2_data;codsch_gv2;gv2_data;codsch_hv3;hv3_data;codsch_gv3;gv3_data;codsch_hv4;hv_data;codsh_gv4;gv4_data


class InduImport(models.Model):
    id_ls = models.CharField(
        max_length=50, verbose_name='Лицевой счет', null=True, blank=True)
    name_dom = models.CharField(
        max_length=50, verbose_name='Номер дома', null=True, blank=True)
    name_kv = models.CharField(
        max_length=50, verbose_name='Квартира', null=True, blank=True)
    codsch_hv1 = models.CharField(
        max_length=50, verbose_name='Код счетчика ХВ_1', null=True, blank=True)
    hv1_data = models.CharField(
        max_length=50, verbose_name='Показание ХВ_1', null=True, blank=True)
    codsh_gv1 = models.CharField(
        max_length=50, verbose_name='Код счетчика ГВ_1', null=True, blank=True)
    gv1_data = models.CharField(
        max_length=50, verbose_name='Показания ГВ_1', null=True, blank=True)
    codsch_hv2 = models.CharField(
        max_length=50, verbose_name="Код счетчика ХВ_2", null=True, blank=True)
    hv2_data = models.CharField(
        max_length=50, verbose_name="Показание ХВ_2", null=True, blank=True)
    codsch_gv2 = models.CharField(
        max_length=20, verbose_name='Код счетчика ГВ_2', null=True, blank=True)
    gv2_data = models.CharField(
        max_length=50, verbose_name='Показание ГВ_2', null=True, blank=True)
    codsch_hv3 = models.CharField(
        max_length=50, verbose_name='Код счетчика ХВ_3', null=True, blank=True)
    hv3_data = models.CharField(
        max_length=50, verbose_name="Показакние ХВ_3", null=True, blank=True)
    codsch_gv3 = models.CharField(
        max_length=50, verbose_name="Код счетчика ГВ_3", null=True, blank=True)
    gv3_data = models.CharField(
        max_length=50, verbose_name="Показания ГВ_3", null=True, blank=True)
    codsch_hv4 = models.CharField(
        max_length=50, verbose_name="Код счетчика ХВ_4", null=True, blank=True)
    hv_data = models.CharField(
        max_length=50, verbose_name='Показания ХВ_4', null=True, blank=True)
    codsh_gv4 = models.CharField(
        max_length=50, verbose_name="Код счетчика ГВ_4", null=True, blank=True)
    gv4_data = models.CharField(
        max_length=50, verbose_name="Показание ГВ_4", null=True, blank=True)

    def __str__(self):
        self.gudvin = "Загрузка показаний на ермак"

        return self.id_ls

    class Meta:
        verbose_name = 'Лицевой'
        verbose_name_plural = 'MKD Лицевые загрузить'


class InduExport(models.Model):
    id_ls = models.CharField(
        max_length=50, verbose_name='Лицевой счет', null=True, blank=True)
    name_dom = models.CharField(
        max_length=50, verbose_name='Номер дома', null=True, blank=True)
    name_kv = models.CharField(
        max_length=50, verbose_name='Квартира', null=True, blank=True)
    codsch_hv1 = models.CharField(
        max_length=50, verbose_name='Код счетчика ХВ_1', null=True, blank=True)
    hv1_data = models.FloatField(
        max_length=50, verbose_name='Показание ХВ_1', null=True, blank=True)
    codsh_gv1 = models.CharField(
        max_length=50, verbose_name='Код счетчика ГВ_1', null=True, blank=True)
    gv1_data = models.FloatField(
        max_length=50, verbose_name='Показания ГВ_1', null=True, blank=True)
    codsch_hv2 = models.CharField(
        max_length=50, verbose_name="Код счетчика ХВ_2", null=True, blank=True)
    hv2_data = models.FloatField(
        max_length=50, verbose_name="Показание ХВ_2", null=True, blank=True)
    codsch_gv2 = models.CharField(
        max_length=20, verbose_name='Код счетчика ГВ_2', null=True, blank=True)
    gv2_data = models.FloatField(
        max_length=50, verbose_name='Показание ГВ_2', null=True, blank=True)
    codsch_hv3 = models.CharField(
        max_length=50, verbose_name='Код счетчика ХВ_3', null=True, blank=True)
    hv3_data = models.FloatField(
        max_length=50, verbose_name="Показакние ХВ_3", null=True, blank=True)
    codsch_gv3 = models.CharField(
        max_length=50, verbose_name="Код счетчика ГВ_3", null=True, blank=True)
    gv3_data = models.FloatField(
        max_length=50, verbose_name="Показания ГВ_3", null=True, blank=True)
    codsch_hv4 = models.CharField(
        max_length=50, verbose_name="Код счетчика ХВ_4", null=True, blank=True)
    hv_data = models.FloatField(
        max_length=50, verbose_name='Показания ХВ_4', null=True, blank=True)
    codsh_gv4 = models.CharField(
        max_length=50, verbose_name="Код счетчика ГВ_4", null=True, blank=True)
    gv4_data = models.FloatField(
        max_length=50, verbose_name="Показание ГВ_4", null=True, blank=True)

    def __str__(self):
        self.gudvin = "Передача показаний"
        return self.id_ls

    class Meta:
        verbose_name = 'Лицевой'
        verbose_name_plural = 'MDK Переданные'


class InduExportSela(models.Model):
    id_ls = models.CharField(
        max_length=50, verbose_name='Лицевой счет', null=True, blank=True)
    name_dom = models.CharField(
        max_length=50, verbose_name='Номер дома', null=True, blank=True)
    name_kv = models.CharField(
        max_length=50, verbose_name='Квартира', null=True, blank=True)
    codsch_hv1 = models.CharField(
        max_length=50, verbose_name='Код счетчика ХВ_1', null=True, blank=True)
    hv1_data = models.FloatField(
        max_length=50, verbose_name='Показание ХВ_1', null=True, blank=True)
    codsh_gv1 = models.CharField(
        max_length=50, verbose_name='Код счетчика ГВ_1', null=True, blank=True)
    gv1_data = models.FloatField(
        max_length=50, verbose_name='Показания ГВ_1', null=True, blank=True)
    codsch_hv2 = models.CharField(
        max_length=50, verbose_name="Код счетчика ХВ_2", null=True, blank=True)
    hv2_data = models.FloatField(
        max_length=50, verbose_name="Показание ХВ_2", null=True, blank=True)
    codsch_gv2 = models.CharField(
        max_length=20, verbose_name='Код счетчика ГВ_2', null=True, blank=True)
    gv2_data = models.FloatField(
        max_length=50, verbose_name='Показание ГВ_2', null=True, blank=True)
    codsch_hv3 = models.CharField(
        max_length=50, verbose_name='Код счетчика ХВ_3', null=True, blank=True)
    hv3_data = models.FloatField(
        max_length=50, verbose_name="Показакние ХВ_3", null=True, blank=True)
    codsch_gv3 = models.CharField(
        max_length=50, verbose_name="Код счетчика ГВ_3", null=True, blank=True)
    gv3_data = models.FloatField(
        max_length=50, verbose_name="Показания ГВ_3", null=True, blank=True)
    codsch_hv4 = models.CharField(
        max_length=50, verbose_name="Код счетчика ХВ_4", null=True, blank=True)
    hv_data = models.FloatField(
        max_length=50, verbose_name='Показания ХВ_4', null=True, blank=True)
    codsh_gv4 = models.CharField(
        max_length=50, verbose_name="Код счетчика ГВ_4", null=True, blank=True)
    gv4_data = models.FloatField(
        max_length=50, verbose_name="Показание ГВ_4", null=True, blank=True)

    def __str__(self):
        self.gudvin = "Передача показаний"
        return self.id_ls

    class Meta:
        verbose_name = 'Лицевой'
        verbose_name_plural = 'Села Переданные'


class InduExportCH(models.Model):
    id_ls = models.CharField(
        max_length=50, verbose_name='Лицевой счет', null=True, blank=True)
    name_dom = models.CharField(
        max_length=50, verbose_name='Номер дома', null=True, blank=True)
    name_kv = models.CharField(
        max_length=50, verbose_name='Квартира', null=True, blank=True)
    codsch_hv1 = models.CharField(
        max_length=50, verbose_name='Код счетчика ХВ_1', null=True, blank=True)
    hv1_data = models.FloatField(
        max_length=50, verbose_name='Показание ХВ_1', null=True, blank=True)
    codsh_gv1 = models.CharField(
        max_length=50, verbose_name='Код счетчика ГВ_1', null=True, blank=True)
    gv1_data = models.FloatField(
        max_length=50, verbose_name='Показания ГВ_1', null=True, blank=True)
    codsch_hv2 = models.CharField(
        max_length=50, verbose_name="Код счетчика ХВ_2", null=True, blank=True)
    hv2_data = models.FloatField(
        max_length=50, verbose_name="Показание ХВ_2", null=True, blank=True)
    codsch_gv2 = models.CharField(
        max_length=20, verbose_name='Код счетчика ГВ_2', null=True, blank=True)
    gv2_data = models.FloatField(
        max_length=50, verbose_name='Показание ГВ_2', null=True, blank=True)
    codsch_hv3 = models.CharField(
        max_length=50, verbose_name='Код счетчика ХВ_3', null=True, blank=True)
    hv3_data = models.FloatField(
        max_length=50, verbose_name="Показакние ХВ_3", null=True, blank=True)
    codsch_gv3 = models.CharField(
        max_length=50, verbose_name="Код счетчика ГВ_3", null=True, blank=True)
    gv3_data = models.FloatField(
        max_length=50, verbose_name="Показания ГВ_3", null=True, blank=True)
    codsch_hv4 = models.CharField(
        max_length=50, verbose_name="Код счетчика ХВ_4", null=True, blank=True)
    hv_data = models.FloatField(
        max_length=50, verbose_name='Показания ХВ_4', null=True, blank=True)
    codsh_gv4 = models.CharField(
        max_length=50, verbose_name="Код счетчика ГВ_4", null=True, blank=True)
    gv4_data = models.FloatField(
        max_length=50, verbose_name="Показание ГВ_4", null=True, blank=True)

    def __str__(self):
        self.gudvin = "Передача показаний"
        return self.id_ls

    class Meta:
        verbose_name = 'Лицевой'
        verbose_name_plural = 'ЧС Переданные'
