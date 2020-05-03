from unittest import mock
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.request import Request
from users.admin import CompanyAdmin
from users.models import Company


class TestCompanyAdmin(TestCase):

    @classmethod
    def setUpTestData(cls):
        company = Company.objects.create(name='Company')
        Company.objects.create(name='Company2')

        site = AdminSite()
        cls.ca = CompanyAdmin(Company, site)

        user = mock.Mock(spec=User)
        user.company = company

        cls.request = mock.Mock(spec=Request)
        cls.request.user = user

    def test_hide_foreign_companies(self):
        self.request.user.is_superuser = False
        self.request.user.save()
        assert self.ca.get_queryset(self.request).count() == 1

    def test_show_all_companies_to_superuser(self):
        self.request.user.is_superuser = True
        self.request.user.save()
        assert self.ca.get_queryset(self.request).count() == 2

    @classmethod
    def tearDownClass(cls):
        Company.objects.all().delete()
