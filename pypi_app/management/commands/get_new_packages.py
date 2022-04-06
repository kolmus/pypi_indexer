from time import timezone
from django.core.management.base import BaseCommand

import xml.etree.ElementTree as ET
from datetime import datetime, date
import pytz
import requests
import xmltodict

from pypi_app.models import Item


class Command(BaseCommand):
    def handle(self, *args, **options):

        new_items = []

        url = "https://pypi.org/rss/packages.xml"
        response = requests.get(url)
        data = xmltodict.parse(response.content)["rss"]["channel"]["item"]

        today = date.today()

        for obj in data:
            title = obj["title"][:-14]
            link = obj["link"]
            try:
                guid = obj["guid"]
            except KeyError:
                guid = None
            description = obj["description"]
            try:
                author = obj["author"]
            except KeyError:
                author = None
            pub_date = datetime(
                year=today.year,
                month=today.month,
                day=today.day,
                hour=int(obj["pubDate"].split(":")[0][-2:]),
                minute=int(obj["pubDate"].split(":")[1]),
                second=int(obj["pubDate"].split(":")[2][:1]),
                microsecond=0,
                tzinfo=pytz.UTC,
            )
            controll_set = Item.objects.filter(
                title=title, link=link, guid=guid, author=author, description=description, pub_date=pub_date
            )

            if controll_set.exists():
                continue
            else:
                new_items.append(
                    Item(title=title, link=link, guid=guid, author=author, description=description, pub_date=pub_date)
                )

        # TODO backup db before save to db,
        if new_items:
            new_items_count = Item.objects.bulk_create(new_items, ignore_conflicts=True)
            print(f"New {len(new_items_count)} new items added to db")
        else:
            print("There is no items to add")
