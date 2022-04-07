from time import time
from pypi_app.models import Item
from pypi_indexer.settings import TEST_ITEMS
from random import randint
from datetime import datetime, timedelta, date, time
import pytz

from faker import Faker

faker = Faker("en-US")


def create_fake_items():
    new_items = []
    now = datetime.now().hour
    for i in range(TEST_ITEMS):
        today = datetime(
            tzinfo=pytz.UTC,
            year=date.today().year,
            month=date.today().month,
            day=date.today().day,
            hour=datetime.now().hour,
            minute=datetime.now().minute,
            second=datetime.now().second,
        )
        item = Item(
            title=faker.company(),
            version=f"{randint(0,20)}.{randint(0,20)}.{randint(0,20)}.{randint(0,20)}.{randint(0,20)}",
            link=faker.url(),
            guid=faker.url(),
            description=faker.sentence(),
            author_name=faker.name(),
            author_email=faker.email(),
            pub_date=today + timedelta(hours=(randint(-12, 0)), minutes=(randint(-59, 0))),
        )
        new_items.append(item)
    created_items = Item.objects.bulk_create(new_items)
