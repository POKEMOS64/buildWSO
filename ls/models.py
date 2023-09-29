from django.db import models

# Create your models here.


class LsModels(models.Model):

    data = models.CharField(max_length=201, null=True)
    org = models.CharField(max_length=202, null=True)
    adr_org = models.CharField(max_length=203, null=True)
    innkpp = models.CharField(max_length=204, null=True)
    bank = models.CharField(max_length=205, null=True)
    bic = models.CharField(max_length=206, null=True)
    kc = models.CharField(max_length=207, null=True)
    rsch = models.CharField(max_length=208, null=True)
    predpr = models.CharField(max_length=209, null=True)

    kod_ls = models.CharField(max_length=210, null=True)
    ls = models.CharField(max_length=211, null=True,
                          verbose_name='Лицевой номер')
    adr = models.CharField(max_length=212, null=True, )
    adr_d = models.CharField(max_length=213, null=True)
    fias = models.CharField(max_length=214, null=True)
    fio = models.CharField(max_length=215, null=True, verbose_name='Фамилия')
    o_s = models.CharField(max_length=216, null=True, verbose_name='o_s')
    dom_s = models.CharField(max_length=217, null=True)
    koplate = models.CharField(max_length=218, null=True)
    peni = models.CharField(max_length=219, null=True)
    name_met1 = models.CharField(
        max_length=220, null=True, verbose_name='Счетчик')
    n_met1 = models.CharField(max_length=221, null=True, verbose_name='Номер')
    cou_met1 = models.CharField(max_length=222, null=True)
    date_met1 = models.CharField(max_length=223, null=True)
    name_met2 = models.CharField(
        max_length=224, null=True, verbose_name='Счетчик')
    n_met2 = models.CharField(max_length=225, null=True, verbose_name='Номер')
    cou_met2 = models.CharField(max_length=226, null=True)
    date_met2 = models.CharField(max_length=227, null=True)
    name_met3 = models.CharField(
        max_length=228, null=True, verbose_name='Счетчик')
    n_met3 = models.CharField(max_length=229, null=True, verbose_name='Номер')
    cou_met3 = models.CharField(max_length=230, null=True)
    date_met3 = models.CharField(max_length=231, null=True)
    name_met4 = models.CharField(
        max_length=232, null=True, verbose_name='Счетчик')
    n_met4 = models.CharField(max_length=233, null=True, verbose_name='Номер')
    cou_met4 = models.CharField(max_length=234, null=True)
    date_met4 = models.CharField(max_length=235, null=True)
    name_met5 = models.CharField(
        max_length=236, null=True, verbose_name='Счетчик')
    n_met5 = models.CharField(max_length=237, null=True, verbose_name='Номер')
    cou_met5 = models.CharField(max_length=238, null=True)
    date_met5 = models.CharField(max_length=239, null=True)
    name_met6 = models.CharField(
        max_length=240, null=True, verbose_name='Счетчик')
    n_met6 = models.CharField(max_length=199, null=True, verbose_name='Номер')
    cou_met6 = models.CharField(max_length=198, null=True)
    date_met6 = models.CharField(max_length=197, null=True)
    kol_prog = models.CharField(max_length=196, null=True)
    str_met = models.CharField(max_length=195, null=True)
    nach_11 = models.CharField(max_length=194, null=True)
    nach_21 = models.CharField(max_length=193, null=True)
    nach_31 = models.CharField(max_length=192, null=True)
    nach_41 = models.CharField(max_length=191, null=True)
    nach_51 = models.CharField(max_length=190, null=True)
    nach_61 = models.CharField(max_length=189, null=True)
    nach_71 = models.CharField(max_length=188, null=True)
    nach_81 = models.CharField(max_length=187, null=True)
    nach_91 = models.CharField(max_length=186, null=True)
    nach_101 = models.CharField(max_length=185, null=True)
    nach_12 = models.CharField(max_length=184, null=True)
    nach_22 = models.CharField(max_length=183, null=True)
    nach_32 = models.CharField(max_length=182, null=True)
    nach_42 = models.CharField(max_length=181, null=True)
    nach_52 = models.CharField(max_length=180, null=True)
    nach_62 = models.CharField(max_length=150, null=True)
    nach_72 = models.CharField(max_length=151, null=True)
    nach_82 = models.CharField(max_length=152, null=True)
    nach_92 = models.CharField(max_length=153, null=True)
    nach_102 = models.CharField(max_length=154, null=True)
    nach_13 = models.CharField(max_length=155, null=True)
    nach_23 = models.CharField(max_length=156, null=True)
    nach_33 = models.CharField(max_length=157, null=True)
    nach_43 = models.CharField(max_length=158, null=True)
    nach_53 = models.CharField(max_length=160, null=True)
    nach_63 = models.CharField(max_length=161, null=True)
    nach_73 = models.CharField(max_length=162, null=True)
    nach_83 = models.CharField(max_length=163, null=True)
    nach_93 = models.CharField(max_length=164, null=True)
    nach_103 = models.CharField(max_length=165, null=True)
    nach_14 = models.CharField(max_length=166, null=True)
    nach_24 = models.CharField(max_length=167, null=True)
    nach_34 = models.CharField(max_length=168, null=True)
    nach_44 = models.CharField(max_length=169, null=True)
    nach_54 = models.CharField(max_length=170, null=True)
    nach_64 = models.CharField(max_length=171, null=True)
    nach_74 = models.CharField(max_length=172, null=True)
    nach_84 = models.CharField(max_length=173, null=True)
    nach_94 = models.CharField(max_length=174, null=True)
    nach_104 = models.CharField(max_length=175, null=True)
    nach_200 = models.CharField(max_length=176, null=True)
    nach_25 = models.CharField(max_length=177, null=True)
    nach_35 = models.CharField(max_length=178, null=True)
    nach_45 = models.CharField(max_length=179, null=True)
    nach_55 = models.CharField(max_length=180, null=True)
    nach_65 = models.CharField(max_length=200, null=True)
    nach_75 = models.CharField(max_length=201, null=True)
    nach_85 = models.CharField(max_length=202, null=True)
    nach_95 = models.CharField(max_length=203, null=True)
    nach_105 = models.CharField(max_length=204, null=True)
    nach_16 = models.CharField(max_length=205, null=True)
    nach_26 = models.CharField(max_length=206, null=True)
    nach_36 = models.CharField(max_length=207, null=True)
    nach_46 = models.CharField(max_length=208, null=True)
    nach_56 = models.CharField(max_length=209, null=True)
    nach_66 = models.CharField(max_length=210, null=True)
    nach_76 = models.CharField(max_length=211, null=True)
    nach_86 = models.CharField(max_length=212, null=True)
    nach_96 = models.CharField(max_length=213, null=True)
    nach_106 = models.CharField(max_length=214, null=True)
    nach_27 = models.CharField(max_length=215, null=True)
    nach_37 = models.CharField(max_length=216, null=True)
    nach_47 = models.CharField(max_length=217, null=True)
    nach_57 = models.CharField(max_length=218, null=True)
    nach_67 = models.CharField(max_length=219, null=True)
    nach_77 = models.CharField(max_length=220, null=True)
    nach_87 = models.CharField(max_length=221, null=True)
    nach_97 = models.CharField(max_length=222, null=True)
    nach_107 = models.CharField(max_length=223, null=True)
    nach_18 = models.CharField(max_length=224, null=True)
    nach_28 = models.CharField(max_length=225, null=True)
    nach_38 = models.CharField(max_length=226, null=True)
    nach_48 = models.CharField(max_length=227, null=True)
    nach_58 = models.CharField(max_length=228, null=True)
    nach_68 = models.CharField(max_length=229, null=True)
    nach_78 = models.CharField(max_length=230, null=True)
    nach_88 = models.CharField(max_length=231, null=True)
    nach_98 = models.CharField(max_length=232, null=True)
    nach_108 = models.CharField(max_length=233, null=True)
    nach_19 = models.CharField(max_length=234, null=True)
    nach_29 = models.CharField(max_length=235, null=True)
    nach_39 = models.CharField(max_length=236, null=True)
    nach_49 = models.CharField(max_length=237, null=True)
    nach_59 = models.CharField(max_length=238, null=True)
    nach_69 = models.CharField(max_length=239, null=True)
    nach_79 = models.CharField(max_length=240, null=True)
    nach_89 = models.CharField(max_length=241, null=True)
    nach_99 = models.CharField(max_length=242, null=True)
    nach_109 = models.CharField(max_length=243, null=True)
    nach_110 = models.CharField(max_length=244, null=True)
    nach_210 = models.CharField(max_length=245, null=True)
    nach_310 = models.CharField(max_length=246, null=True)
    nach_410 = models.CharField(max_length=247, null=True)
    nach_510 = models.CharField(max_length=248, null=True)
    nach_610 = models.CharField(max_length=249, null=True)
    nach_710 = models.CharField(max_length=250, null=True)
    nach_810 = models.CharField(max_length=251, null=True)
    nach_910 = models.CharField(max_length=252, null=True)
    nach_1010 = models.CharField(max_length=253, null=True)
    nach_111 = models.CharField(max_length=254, null=True)
    nach_211 = models.CharField(max_length=255, null=True)
    nach_311 = models.CharField(max_length=255, null=True)
    nach_411 = models.CharField(max_length=255, null=True)
    nach_511 = models.CharField(max_length=255, null=True)
    nach_611 = models.CharField(max_length=255, null=True)
    nach_711 = models.CharField(max_length=255, null=True)
    nach_811 = models.CharField(max_length=255, null=True)
    nach_911 = models.CharField(max_length=255, null=True)
    nach_1011 = models.CharField(max_length=255, null=True)
    nach_112 = models.CharField(max_length=255, null=True)
    nach_212 = models.CharField(max_length=255, null=True)
    nach_312 = models.CharField(max_length=255, null=True)
    nach_412 = models.CharField(max_length=255, null=True)
    nach_512 = models.CharField(max_length=255, null=True)
    nach_612 = models.CharField(max_length=255, null=True)
    nach_712 = models.CharField(max_length=255, null=True)
    nach_812 = models.CharField(max_length=255, null=True)
    nach_912 = models.CharField(max_length=255, null=True)
    nach_1012 = models.CharField(max_length=255, null=True)
    nach_113 = models.CharField(max_length=255, null=True)
    nach_213 = models.CharField(max_length=255, null=True)
    nach_313 = models.CharField(max_length=255, null=True)
    nach_413 = models.CharField(max_length=255, null=True)
    nach_513 = models.CharField(max_length=255, null=True)
    nach_613 = models.CharField(max_length=255, null=True)
    nach_713 = models.CharField(max_length=255, null=True)
    nach_813 = models.CharField(max_length=255, null=True)
    nach_913 = models.CharField(max_length=255, null=True)
    nach_1013 = models.CharField(max_length=255, null=True)
    nach_114 = models.CharField(max_length=255, null=True)
    nach_214 = models.CharField(max_length=255, null=True)
    nach_314 = models.CharField(max_length=255, null=True)
    nach_414 = models.CharField(max_length=255, null=True)
    nach_514 = models.CharField(max_length=255, null=True)
    nach_614 = models.CharField(max_length=255, null=True)
    nach_714 = models.CharField(max_length=255, null=True)
    nach_814 = models.CharField(max_length=255, null=True)
    nach_914 = models.CharField(max_length=255, null=True)
    nach_1014 = models.CharField(max_length=255, null=True)
    it_sumnach = models.CharField(max_length=255, null=True)
    it_sumpeni = models.CharField(max_length=255, null=True)
    it_dolg = models.CharField(max_length=255, null=True)
    it_opl = models.CharField(max_length=255, null=True)
    pred_plat = models.CharField(max_length=255, null=True)
    info1 = models.CharField(max_length=255, null=True)
    info2 = models.CharField(max_length=255, null=True)
    qr1 = models.CharField(max_length=255, null=True)
    qr = models.CharField(max_length=255, null=True)
    

    def __str__(self):
        return self.ls


class mkdLsList(models.Model):
    id_ls = models.CharField(max_length=100, verbose_name='Лицевой МКД')

    def __str__(self):
        return self.id_ls

    class Meta:
        verbose_name = 'Лицевой счет МКД'
        verbose_name_plural = 'Лицевой счет МКД'


class selaLsList(models.Model):
    id_ls = models.CharField(max_length=100, verbose_name='Лицевой Села')

    def __str__(self):
        return self.id_ls

    class Meta:
        verbose_name = 'Лицевой счет Села'
        verbose_name_plural = 'Лицевой счет Села'


class chLsList(models.Model):
    id_ls = models.CharField(
        max_length=100, verbose_name='Лицевой Частный сектор')

    def __str__(self):
        return self.id_ls

    class Meta:
        verbose_name = 'Лицевой счет Частный сектор'
        verbose_name_plural = 'Лицевой счет Частный сектор'
