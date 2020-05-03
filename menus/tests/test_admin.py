from unittest import mock
from django.contrib.admin import AdminSite
from django.test import TestCase
from rest_framework.request import Request
from menus.models import Menu, Dish
from menus.admin import MenuAdmin, DishAdmin
from users.models import Company, User


class TestMenuAdmin(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.site = AdminSite()
        cls.company = Company.objects.create(name='Company')
        company2 = Company.objects.create(name='Company2')

        cls.menu = Menu.objects.create(name='Menu', company=cls.company)
        cls.menu2 = Menu.objects.create(name='Menu2', company=company2)

        cls.ma = MenuAdmin(Menu, cls.site)
        super(TestMenuAdmin, cls).setUpClass()

    def setUp(self):

        user = mock.Mock(spec=User)
        user.company = self.company

        self.request = mock.Mock(spec=Request)
        self.request.user = user
        self.real_request = Request

    def test_hide_foreign_menus(self):
        self.request.user.is_superuser = False
        self.request.user.save()
        assert self.ma.get_queryset(self.request).count() == 1

    def test_show_all_menus_to_superuser(self):
        self.request.user.is_superuser = True
        self.request.user.save()
        assert self.ma.get_queryset(self.request).count() == 2

    @classmethod
    def tearDownClass(cls):
        Company.objects.all().delete()
        Menu.objects.all().delete()


class TestDishAdmin(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.site = AdminSite()

        cls.company = Company.objects.create(name='Company')
        company2 = Company.objects.create(name='Company2')

        cls.dish = Dish.objects.create(name='Dish1', company=cls.company, price=10, preparation_time='15min')
        cls.dish2 = Dish.objects.create(name='Dish2', company=company2, price=10, preparation_time='15min')

        cls.da = DishAdmin(Dish, cls.site)

        user = mock.Mock(spec=User)
        user.company = cls.company

        cls.request = mock.Mock(spec=Request)
        cls.request.user = user

    def test_hide_foreign_dishes(self):
        self.request.user.is_superuser = False
        self.request.user.save()
        assert self.da.get_queryset(self.request).count() == 1

    def test_show_all_dishes_to_superuser(self):
        self.request.user.is_superuser = True
        self.request.user.save()
        assert self.da.get_queryset(self.request).count() == 2

    @classmethod
    def tearDownClass(cls):
        Company.objects.all().delete()
        Dish.objects.all().delete()