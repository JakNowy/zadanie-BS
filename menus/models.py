from PIL import Image
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe

from utils.db import DateTimeMixin


class Menu(DateTimeMixin):
    name = models.CharField(max_length=128, verbose_name='Nazwa')
    description = models.TextField(null=True, blank=True, verbose_name='Opis')
    company = models.ForeignKey('users.Company', on_delete=models.DO_NOTHING, related_name='menus', null=False, verbose_name='Firmy')
    dishes = models.ManyToManyField('Dish', related_name='menus', verbose_name='Dania')

    def __str__(self):
        return f'{self.company.name}: {self.name}'

    def company_name(self):
        return self.company.name

    def dish_count(self):
        return self.dishes.count()

    class Meta:
        verbose_name = 'Karta'
        verbose_name_plural = 'Karty'


class Dish(DateTimeMixin):
    name = models.CharField(max_length=128, unique=True, verbose_name='Nazwa')
    description = models.TextField(null=True, blank=True, verbose_name='Opis')
    company = models.ForeignKey('users.Company', on_delete=models.DO_NOTHING, related_name='dishes', null=True, verbose_name='Firma')
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=(MinValueValidator(0), ), verbose_name='Cena')
    preparation_time = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Czas przygotowania')
    is_vegan = models.BooleanField(default=False, verbose_name='Wegańskie')
    image = models.ImageField(upload_to='dishes/', null=True, blank=True, verbose_name='Zdjęcie')

    image_size = 100

    class Meta:
        verbose_name = 'Danie'
        verbose_name_plural = 'Dania'

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        # Crop the image if it's bigger than needed.
        super().save(**kwargs)

        if self.image:
            img = Image.open(self.image.path)
            if img.height > self.image_size or img.width > self.image_size:
                img.thumbnail((self.image_size, self.image_size))
                img.save(self.image.path)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="%s" height="%s" />'
                         % (self.image, self.image_size, self.image_size)) if self.image else None

    image_tag.short_description = 'Image'
