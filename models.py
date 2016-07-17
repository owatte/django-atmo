# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    These data are store as string to prevent some error because of time
    settings on the local machine.
    - date_tomorrow is not stored.
    - a record_date field is added to store the indice atmo record datetime
    """

    INDICE_CHOICES = zip(range(1, 10), range(1, 10))
    config_date = models.CharField(blank=False, max_length=10)
    date_today = models.CharField(blank=False, max_length=10)
    today = models.PositiveSmallIntegerField(
        choices=INDICE_CHOICES, blank=True
    )
    tomorrow = models.PositiveSmallIntegerField(
        choices=INDICE_CHOICES, blank=True
    )
    record_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[{0}] {1}'.format(
            str(self.today), self.record_date.strftime("%A %d %B %Y [%H:%M]")
        )

    class Meta:
        ordering = ['-record_date']
        verbose_name = 'indice ATMO'
        verbose_name_plural = 'indices ATMO'

class Station(models.Model):
    u"""Station, based on ISEO description.

    [{"nressurv":"37","nsit":"001","isit":"ST de Baie mahault  "},{"nressurv":"37","nsit":"002","isit":"ST de Pointe \u00e0 Pitre"},{"nressurv":"37","nsit":"003","isit":"ST des Abymes       "},{"nressurv":"37","nsit":"004","isit":"STATION MOB D\u00e9sirade"},{"nressurv":"37","nsit":"005","isit":"ST Industrielle     "}]
    """
    # # network
    # nressurv = models.PositiveSmallIntegerField(blank=False)
    # # station ID
    # nsit = models.PositiveSmallIntegerField(blank=False)
    # # station label
    # isit = models.CharField(max_length=30, blank=False)
    network = models.CharField(max_length=30)
    ident = models.CharField(max_length=10, blank=False, unique=True)
    label = models.CharField(max_length=30)
    date_start = models.DateTimeField(blank=False)
    date_stop = models.DateTimeField(null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=False)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=False)
    alt = models.PositiveSmallIntegerField(blank=False)
    last_update = models.DateTimeField(null=True)
    record_date = models.DateTimeField(auto_now_add=True)

    def ident(self):
        return '{0}{1}'.format(str(self.nressurv), str(self.nsit).zfill(3))

    def __str__(self):
        return '[{0}] {1}'.format(self.ident, self.isit)

class Params(models.Model):
    station = models.ForeignKey('Station', on_delete=models.CASCADE)
    # eg. "cchim": "dioxyde de soufre"
    cchim = models.CharField(max_length=35)
    # eg. "unit": "microg\/m3 "
    unit = models.CharField(max_length=25)
    # eg. "nopol": "08"
    nopol = models.PositiveSmallIntegerField
    # eg. "cmet": "A" found only A S 1 or ""
    cmet = models.CharField(max_length=5)
    # eg  "last_value": null or "last_value": "23-06-2011 07:45:00"
    last_value = models.DateTimeField()
    record_date = models.DateTimeField(auto_now_add=True)
