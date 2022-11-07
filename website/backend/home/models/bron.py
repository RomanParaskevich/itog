from django.db import models


class Bron(models.Model):
    date_in = models.DateField(verbose_name='Дата заезда', blank=True, null=True)
    date_out = models.DateField(verbose_name='Дата выезда', blank=True, null=True)
    adults = models.PositiveSmallIntegerField(verbose_name='Взрослые')
    kids = models.PositiveSmallIntegerField(verbose_name='Дети')
