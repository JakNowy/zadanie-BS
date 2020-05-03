from django.core.management.base import BaseCommand
from menus.models import Menu, Dish
from users.models import Company


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

        # POSITIONAL ARGUMENTS
        # parser.add_argument('start', nargs=1, type=int)

        # OPTIONAL ARGUMENTS
        # Log on console
        # parser.add_argument('--log', action='store_true')

    def handle(self, *args, **options):

        # COMPANIES
        company_names = ['Manekin', 'Mandu', 'Lee\'s Chineese', 'Piqniq', 'Śliwka w kompot']
        for company in company_names:
            Company.objects.get_or_create(name=company)
        print('Companies created!')

        manekin = Company.objects.get(name='Manekin')
        sliwka = Company.objects.get(name='Śliwka w kompot')

        # DISHES
        dishes = [
            {'name': 'Naleśnik z serem', 'price': 10, 'description': 'Ale pyszne!', 'company': manekin,
             'is_vegan': True},
            {'name': 'Naleśnik z wołowiną', 'price': 15, 'description': 'Ale pyszne!', 'company': manekin,
             'is_vegan': False},
            {'name': 'Naleśnik z truskawkami', 'price': 12, 'description': 'Ale pyszne!', 'company': manekin,
             'is_vegan': True},
            {'name': 'Naleśnik z łososiem', 'price': 10, 'description': 'Ale pyszne!', 'company': manekin,
             'is_vegan': False},
            {'name': 'Ośmiornica', 'price': 10, 'description': 'Ale pyszne!', 'company': sliwka,
             'is_vegan': False},
            {'name': 'Żeberka z dzika', 'price': 10, 'description': 'Ale pyszne!', 'company': sliwka,
             'is_vegan': False},
            {'name': 'Karkówka w sosie miodowo-musztardowym', 'price': 10, 'description': 'Ale pyszne!', 'company': sliwka,
             'is_vegan': False},
        ]

        for dish in dishes:
            dish_name = dish.pop('name')
            Dish.objects.get_or_create(name=dish_name, defaults=dish)
        print('Dishes created!')

        dish1 = Dish.objects.first()
        dish2 = Dish.objects.last()

        # MENUS
        menus = [
            {'name': 'Menu letnie', 'description': 'Lorem20', 'company': manekin},
            {'name': 'Menu jesienne', 'description': 'Lorem20', 'company': manekin},
            {'name': 'Menu wiosenne', 'description': 'Lorem20', 'company': manekin},
            {'name': 'Menu zimowe', 'description': 'Lorem20', 'company': manekin},
            {'name': 'Menu kwiecien', 'description': 'Lorem20', 'company': sliwka},
            {'name': 'Menu maj', 'description': 'Lorem20', 'company': sliwka},
            {'name': 'Menu czerwiec', 'description': 'Lorem20', 'company': sliwka},
            {'name': 'Menu lipiec', 'description': 'Lorem20', 'company': sliwka},
        ]
        for menu in menus:
            menu_name = menu.pop('name')
            m, _ = Menu.objects.get_or_create(name=menu_name, defaults=menu)
            m.dishes.add(dish1)
            m.dishes.add(dish2)
            m.save()
        print('Menus created!')
