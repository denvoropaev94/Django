from django.core.management.base import BaseCommand
from lesson2.models import User


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **options):
        # user = User(name=' Den', email='denn@example.com', password='secret', age=28)
        # user = User(name=' Nik', email='nikitka@mail.com', password='trtrtr', age=29)
        user = User(name=' Oleg', email='olegka@gmail.com', password='bulling', age=35)
        user.save()
        self.stdout.write(f'{user}')
