import random
from django.core.management.base import BaseCommand
from menus.models import Menu, Dish
from users.models import Company, User


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

        # POSITIONAL ARGUMENTS
        # parser.add_argument('start', nargs=1, type=int)

        # OPTIONAL ARGUMENTS
        # Log on console
        # parser.add_argument('--log', action='store_true')

    def handle(self, *args, **options):

        User.objects.all().delete()
        Menu.objects.all().delete()
        Dish.objects.all().delete()
        Company.objects.all().delete()
