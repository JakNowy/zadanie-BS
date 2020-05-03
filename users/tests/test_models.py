from unittest import TestCase
from users.models import Company


class TestCompanyModel(TestCase):

    def test_company__str__(self):
        company = Company.objects.create(name='Company')
        assert company.__str__() == company.name

    @classmethod
    def tearDownClass(cls):
        Company.objects.all().delete()
