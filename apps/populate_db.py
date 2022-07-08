# population.py file
import os

from faker.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django

django.setup()

import random
from apps.users.models import User
from courses.models import Tag, Course
from faker import Faker
from faker.generator import random

Faker.seed(50)
fakegen = Faker()


def generate_tags(n=10):
    tags = ['django', 'web', 'app', 'course', 'programming']

    for _ in range(n):
        fake_name = random.choice([tag for tag in tags])
        fake_slug = slugify(fake_name)
        if not Tag.objects.filter(slug=fake_slug).exists():
            tag = Tag(
                name=fake_name,
                slug=fake_slug
            )
            tag.save()


def generate_course(n):
    course_categories = ['Search', 'Social', 'Marketplace', 'News', 'Games']
    from django.utils.timezone import get_current_timezone

    tzinfo = get_current_timezone()
    for _ in range(n):
        f_title = fakegen.sentence(nb_words=3)
        f_rating = random.randint(1, 5)
        f_price = round(random.uniform(10 ** 3, 10 ** 7), 2)
        f_in = fakegen.date_time(tzinfo=tzinfo)
        f_out = fakegen.date_time(tzinfo=tzinfo)
        users = User.objects.all()
        f_author = random.choice(users)
        f_description = fakegen.paragraph(nb_sentences=5)
        f_logo = fakegen.image_url()
        f_picture = fakegen.image_url()
        f_tags = random.choices(Tag.objects.all(), k=random.randint(1, 5))
        f_email = fakegen.email()
        # f_user = random.choice(all_users)
        # creating data object and saving to DB
        course = Course.objects.create(
            title=f_title,
            rating=f_rating,
            price=f_price,
            _in=f_in,
            out=f_out,
            author=f_author,
            description=f_description,
            logo=f_logo,
            picture=f_picture,
        )
        for tag in f_tags:
            course.tags.add(tag)
        print(f'{_} created course')


# generate_tags()
generate_course(100_000)
#
# def add_topic():
#     t = Course.objects.get_or_create(top_name=random.choice(course_categories))[0]
#     t.save()
#     return t


# def populate(N=10):
#     for entry in range(N):
#         top = add_topic()
#
#         fake_url = fakegen.url()
#         fake_date = fakegen.date()
#         fake_name = fakegen.company()
#
#         webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
#
#         acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


# def populate_tags(n=10):
# for _ in range(n):
#     fake_name = fakegen
#     self.slug = slugify(self.title)


# populate(20)
