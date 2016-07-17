# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class IndiceAtmo(models.Model):
    u"""The Indice Atmo table.

    Based on the ISEO indiceatmo.json :
    {"today":"4",
    "tomorrow":"5",
    "config_date":"2016-07-15",
    "date_today":"2016-07-15",
    "date_tomorrow":"16 Jul 2016"}

    - today and tomorrow can be blank in case of missing data.
    - config_date and date_today are both stored, to be able to process a date
    checking and maybe to determine the UTC parameter or report rolling time.
    These data are store as string to prevent some error because of time settings
    on the local machine.
    - date_tomorrow is not stored.
    - a record_date field is added to store the indice atmo datetime
    """

    INDICE_CHOICES = zip(range(1, 10), range(1, 10))
    config_date = models.CharField(blank=False, max_length=10)
    date_today = models.CharField(blank=False,  max_length=10)
    today = models.PositiveSmallIntegerField(
        choices=INDICE_CHOICES, blank=True
    )
    tomorrow = models.PositiveSmallIntegerField(
        choices=INDICE_CHOICES, blank=True
    )
    record_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-record_date']
        verbose_name = 'indice ATMO'
        verbose_name_plural = 'indices ATMO'
