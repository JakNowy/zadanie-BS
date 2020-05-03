from PIL import Image
from django.db import models
from django.utils.safestring import mark_safe


class Menu(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    company = models.ForeignKey('users.Company', on_delete=models.DO_NOTHING, related_name='menus', null=False)
    dishes = models.ManyToManyField('Dish', related_name='menus')
    date_modified = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.company.name}: {self.name}'


class Dish(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    company = models.ForeignKey('users.Company', on_delete=models.DO_NOTHING, related_name='dishes', null=True)
    price = models.FloatField()
    preparation_time = models.CharField(max_length=16)
    is_vegan = models.BooleanField(default=False)
    image = models.ImageField(upload_to='dishes/', null=True, blank=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now=True)

    image_size = 100

    class Meta:
        verbose_name_plural = 'Dishes'

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
