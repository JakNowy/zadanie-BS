from django.test import TestCase
from django.urls import reverse
from menus.models import Menu, Dish
from users.models import Company


class TestMenuViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        company1 = Company.objects.create(name='Company')
        company2 = Company.objects.create(name='Company2')
       
        menu1 = Menu.objects.create(name="Menu", company=company1, description='')
        menu2 = Menu.objects.create(name="Zmenu", company=company1, description='')

        dish1 = Dish.objects.create(name='Dish1', company=company2, price=10, preparation_time='15min')
        dish2 = Dish.objects.create(name='Dish2', company=company1, price=10, preparation_time='15min')
        dish3 = Dish.objects.create(name='Dish3', company=company1, price=10, preparation_time='15min')

        dish1.menus.add(menu2)
        dish2.menus.add(menu2)
        dish3.menus.add(menu1)

        cls.menu1 = menu1

    def test_forbid_menu_create(self):
        url = reverse('menu-list')
        data = {'name': 'New Menu', 'company_id': 1, 'description': ''}
        response = self.client.post(url, data, format='json')
        assert response.status_code == 405

    def test_retrieve_menu_list(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_retrieve_menu_detail(self):
        url = reverse('menu-detail', kwargs={'pk': self.menu1.pk})
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data.get('name') == 'Menu'

    def test_retrieve_menu_orderring_name(self):
        url = reverse('menu-list')
        url += '?orderring=-name'
        response = self.client.get(url)
        assert response.data.get('results')[0].get('name') == 'Zmenu'
        assert response.data.get('results')[1].get('name') == 'Menu'

    def test_retrieve_menu_orderring_dish_count(self):
        url = reverse('menu-list')
        url += '?orderring=-dish_count'
        response = self.client.get(url)
        assert response.data.get('results')[0].get('name') == 'Zmenu'
        assert response.data.get('results')[1].get('name') == 'Menu'

    def test_forbid_menu_update(self):
        url = reverse('menu-list')
        data = {'name': 'New Menu', 'company_id': 1, 'description': ''}
        response = self.client.patch(url, data, format='json')
        assert response.status_code == 405

    def test_forbid_menu_delete(self):
        url = reverse('menu-detail', kwargs={'pk': self.menu1.pk})
        response = self.client.delete(url)
        assert response.status_code == 405

    @classmethod
    def tearDownClass(cls):
        Menu.objects.all().delete()
        Company.objects.all().delete()
        Dish.objects.all().delete()


class TestDishViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        company1 = Company.objects.create(name='Company')
        cls.dish1 = Dish.objects.create(name='Dish1', company=company1, price=10, preparation_time='15min')

    def test_retrieve_dish_list(self):
        url = reverse('dish-list')
        response = self.client.post(url, format='json')
        assert response.status_code == 405

    def test_retrieve_dish_detail(self):
        url = reverse('dish-detail', kwargs={'pk': self.dish1.pk})
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data.get('name') == 'Dish1'

    @classmethod
    def tearDownClass(cls):
        Company.objects.all().delete()
        Dish.objects.all().delete()
