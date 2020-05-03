from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    company = models.ForeignKey('Company', on_delete=models.DO_NOTHING, related_name='users', null=True)


class Company(models.Model):
    name = models.CharField(max_length=128)
    current_menu = models.ForeignKey('menus.Menu', on_delete=models.CASCADE, related_name='current_company', null=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
