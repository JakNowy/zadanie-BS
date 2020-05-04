import os
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils.safestring import mark_safe
from menus.models import Dish, Menu
from users.models import Company


class TestDishModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        image = Image.new(mode="RGB", size=(200, 200), color=(256, 0, 0))
        image.save('test.jpg')
        cls.image = SimpleUploadedFile(name='test.jpg', content=open('test.jpg', 'rb').read(),
                                             content_type='image/jpeg')

    def setUp(self):
        self.dish = Dish.objects.create(name='Dish3', price=10, preparation_time='15min')

    def test_dish__str__(self):
        assert self.dish.__str__() == 'Dish3'

    def test_image_cropped(self):
        self.dish.image = self.image
        self.dish.save()
        image = Image.open(self.dish.image)
        assert image.size == (self.dish.image_size, self.dish.image_size)

    def test_image_tag(self):
        self.dish.image = self.image
        self.dish.save()

        assert self.dish.image_tag() == mark_safe('<img src="/media/%s" width="%s" height="%s" />'
                                                % (self.dish.image, self.dish.image_size, self.dish.image_size))

    def test_image_tag_none(self):
        self.dish.save()
        assert not self.dish.image_tag()

    @classmethod
    def tearDownClass(cls):
        Dish.objects.all().delete()
        os.remove('test.jpg')

        # os.remove('media/dishes/test')
        # Sometimes randomly complains about access denied to file.
        # Tested on Win10. On Linux "CHMOD 777" is likely to fix it.


class TestMenuModel(TestCase):

    @classmethod
    def setUpClass(cls):
        dish = Dish.objects.create(name='Dish', price=10)
        company = Company.objects.create(name='Company')
        cls.menu = Menu.objects.create(name='Menu', company=company)
        cls.menu.dishes.add(dish)
        cls.menu.save()

    def test_menu_company_name_resolve(self):
        assert self.menu.company_name() == 'Company'

    def test_menu_dish_count_resolve(self):
        assert self.menu.dish_count() == 1

    def test_menu__str__(self):
        assert self.menu.__str__() == 'Company: Menu'

    @classmethod
    def tearDownClass(cls):
        Company.objects.all().delete()
        Menu.objects.all().delete()
        Dish.objects.all().delete()
