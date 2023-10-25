from django.core.management.base import BaseCommand
from lesson2.models import Authors, Posts


# class Command(BaseCommand):
#     help = "Generate fake authors and posts."
#
#     def add_arguments(self, parser):
#         parser.add_argument('count', type=int, help='User ID')
#
#     def handle(self, *args, **kwargs):
#         count = kwargs.get('count')
#         for i in range(1, count + 1):
#             author = Authors(name=f'Name{i}', email=f'mail{i}@mail.ru')
#             author.save()
#             for j in range(1, count + 1):
#                 post = Posts(
#                     title=f'Title{j}',
#                     content=f'Text from {author.name} #{j} is bla bla bla many long text',
#                     author=author
#                 )
#                 post.save()
class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **options):
        author = Authors(name=' Mike', email='mikk@gmail.com')
        author.save()
        self.stdout.write(f'{author}')

