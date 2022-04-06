from time import timezone
from django.core.management.base import BaseCommand

import xml.etree.ElementTree as ET
from datetime import datetime, date
import pytz

from pypi_app.models import Item


class Command(BaseCommand):
    def handle(self, *args, **options):

        new_items = []

        xml_tree = ET.parse("pypi_app/management/xml/packages.xml")
        xml_root = xml_tree.getroot()

        today = date.today()

        for obj in xml_root[0].findall("item"):
            title = obj.find("title").text[:-14]
            link = obj.find("link").text
            guid = obj.find("guid").text
            description = obj.find("description").text
            try:
                author = obj.find("author").text
            except AttributeError:
                author = None
            pub_date = datetime(
                year=today.year,
                month=today.month,
                day=today.day,
                hour=int(obj.find("pubDate").text.split(":")[0][-2:]),
                minute=int(obj.find("pubDate").text.split(":")[1]),
                second=int(obj.find("pubDate").text.split(":")[2][:1]),
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
