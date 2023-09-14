from django.core.management.base import  BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Create user"

    def handle (self, *args, **kwargs):
        user = User(
            # name = 'John',
            # email = 'EMAIL@example.com',
            # password = 'secret',
            # age = 25,
            # name = 'Neo',
            # email = 'neo@example.com',
            # password = 'secret',
            # age = 29,
            name = 'Jack',
            email = 'jack@example.com',
            password = 'secret',
            age = 47,
        )
        user.save()
        self.stdout.write(f'{user}')
