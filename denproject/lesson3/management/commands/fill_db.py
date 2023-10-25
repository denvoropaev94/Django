from random import choices

from django.core.management.base import BaseCommand
from lesson3.models import Authors, Posts

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
        "Expedita ipsum praesentium quo quos sunt? Accusantium asperiores beatae " \
        "culpa dolorem doloribus eveniet fugit ipsa molestias nemo quibusdam?" \
        "Accusamus consequatur debitis itaque soluta vitae. Ab accusantium aperiam facere impedit ipsum," \
        "officia repudiandae. Accusamus architecto blanditiis commodi culpa cumque cupiditate deserunt " \
        "ducimus eos exercitationem expedita explicabo facilis hic ipsa, ipsam, iusto libero " \
        "molestiae natus neque obcaecati odio odit provident quibusdam quis rem repellendus sapiente " \
        "sit temporibus tenetur unde voluptatem? Ad adipisci aliquam amet aperiam architecto atque " \
        "consectetur error fugiat inventore iure iusto libero, quaerat sunt tempora ut voluptas voluptatibus" \
        "Consequatur esse iusto praesentium."


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count_of_users')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Authors(name=f'Author{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Posts(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64)),
                    author=author
                )
                post.save()
