from django.contrib.auth.models import Permission, Group
from django.core.management.base import BaseCommand
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
        manekin = Company.objects.get(name='Manekin')
        sliwka = Company.objects.get(name='Śliwka w kompot')

        m, _ = User.objects.get_or_create(username='Pan Z Manekina', defaults={
            'is_staff': True,
            'company': manekin
        })
        m.set_password('password')

        s, _ = User.objects.get_or_create(username='Pan Ze Sliwki', defaults={
            'is_staff': True,
            'company': sliwka
        })
        s.set_password('password')

        a, _ = User.objects.get_or_create(username='admin', defaults={
            'is_staff': True,
            'is_superuser': True,
        })
        a.set_password('password')

        # GROUP PERMISSIONS
        group, _ = Group.objects.get_or_create(name='Manager')
        permission_names = ['Can add dish', 'Can change dish', 'Can delete dish', 'Can view dish', 'Can add menu',
                            'Can change menu', 'Can delete menu', 'Can view menu', 'Can add company',
                            'Can change company', 'Can view company']

        for permission_name in permission_names:
            permission = Permission.objects.get(name=permission_name)
            group.permissions.add(permission)

        m.groups.add(group)
        s.groups.add(group)

        m.save()
        s.save()
        a.save()

        print('Admins created and granted permissions.')
