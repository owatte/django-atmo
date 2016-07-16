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
    - date_tomorrow is not stored.
    """

    INDICE_CHOICES = zip(range(1, 10), range(1, 10))
    config_date = models.DateField(blank=False)
    date_today = models.DateField(blank=False)
    today = models.PositiveSmallIntegerField(
        choices=INDICE_CHOICES, blank=True
    )
    tomorrow = models.PositiveSmallIntegerField(
        choices=INDICE_CHOICES, blank=True
    )
    record_date = models.DateTimeField(auto_now_add=True)
