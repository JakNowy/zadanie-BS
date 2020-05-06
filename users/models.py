from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.db import DateTimeMixin


class User(AbstractUser):
    company = models.ForeignKey('Company', on_delete=models.DO_NOTHING, related_name='users', null=True, verbose_name='Firma')

    class Meta:
        verbose_name = 'Użytkownik'
        verbose_name_plural = 'Użytkownicy'


class Company(DateTimeMixin):
    name = models.CharField(max_length=128, verbose_name='Nazwa')
    current_menu = models.ForeignKey('menus.Menu', on_delete=models.CASCADE, related_name='current_company', null=True, verbose_name='Aktualne Menu')

    class Meta:
        verbose_name = 'Firma'
        verbose_name_plural = 'Firmy'

    def __str__(self):
        return self.name
