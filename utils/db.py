from django.db import models
from django.utils.datetime_safe import datetime


class DateTimeMixin(models.Model):
    date_modified = models.DateTimeField(auto_now_add=True, verbose_name='Data modyfikacji')
    date_created = models.DateTimeField(auto_now=True, verbose_name='Data utworzenia')

    class Meta:
        abstract = True
