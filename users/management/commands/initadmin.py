from django.core.management.base import BaseCommand

from users.models import ExtendedUser
from django.conf import settings


class Command(BaseCommand):
    help = "Команда для создания первой учетной записи администратора, если в БД нет пользователей"

    def handle(self, *args, **options):
        if ExtendedUser.objects.count() == 0:
            for user in settings.ADMINS:
                email = user[0]
                password = user[1]
                print('Creating account for %s' % email)
                admin = ExtendedUser.objects.create_superuser(email=email, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
