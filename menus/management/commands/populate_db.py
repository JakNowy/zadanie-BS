import random
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

        dishes_manekin = Dish.objects.filter(company=manekin)
        dishes_sliwka = Dish.objects.filter(company=sliwka)

        # MENUS
        menus = [
            {'name': 'Menu letnie', 'description': 'Wszystko pyszne!', 'company': manekin},
            {'name': 'Menu jesienne', 'description': 'Wszystko pyszne!', 'company': manekin},
            {'name': 'Menu wiosenne', 'description': 'Wszystko pyszne!', 'company': manekin},
            {'name': 'Menu zimowe', 'description': 'Wszystko pyszne!', 'company': manekin},
            {'name': 'Menu kwiecien', 'description': 'Wszystko pyszne!', 'company': sliwka},
            {'name': 'Menu maj', 'description': 'Wszystko pyszne!', 'company': sliwka},
            {'name': 'Menu czerwiec', 'description': 'Wszystko pyszne!', 'company': sliwka},
            {'name': 'Menu lipiec', 'description': 'Wszystko pyszne!', 'company': sliwka},
        ]
        for menu in menus:
            menu_name = menu.pop('name')
            m, _ = Menu.objects.get_or_create(name=menu_name, defaults=menu)

            if m.company == manekin:
                for dish in dishes_manekin:
                    if random.getrandbits(1):
                        m.dishes.add(dish)

            elif m.company == sliwka:
                for dish in dishes_sliwka:
                    if random.getrandbits(1):
                        m.dishes.add(dish)

            m.save()
        print('Menus created!')
