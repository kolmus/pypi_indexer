from django.core.management.base import BaseCommand

from datetime import datetime, date
import pytz
import requests
import xmltodict
from bs4 import BeautifulSoup

from pypi_app.models import Item


class Command(BaseCommand):
    """
    This script fetch .xml file from source and index data into DB.

    Prints result of proces
    """

    def handle(self, *args, **options):
        new_items = []

        url = "https://pypi.org/rss/packages.xml"
        xml_response = requests.get(url)
        data = xmltodict.parse(xml_response.content)["rss"]["channel"]["item"]

        today = date.today()

        for obj in data:

            title = obj["title"][:-14]
            link = obj["link"]
            page = requests.get(link)
            soup = BeautifulSoup(page.text, "html.parser")
            version = soup.find_all("h1", {"class": "package-header__name"})[0].get_text().split(" ")[9][:-1]

            try:
                guid = obj["guid"]
            except KeyError:
                guid = None
            description = obj["description"]
            try:
                author_email = obj["author"]
            except KeyError:
                author_email = None
            try:
                author_name = soup.find_all("a", {"href": f"mailto:{author_email}"})[0].get_text()
            except IndexError:
                author_name = None

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
                title=title,
                link=link,
                guid=guid,
                author_email=author_email,
                description=description,
                pub_date=pub_date,
                version=version,
                author_name=author_name,
            )

            if controll_set.exists():
                continue
            else:
                new_items.append(
                    Item(
                        title=title,
                        version=version,
                        link=link,
                        guid=guid,
                        author_name=author_name,
                        author_email=author_email,
                        description=description,
                        pub_date=pub_date,
                    )
                )

        # TODO backup db before save to db,
        if new_items:
            new_items_count = Item.objects.bulk_create(new_items, ignore_conflicts=True)
            print(f"New {len(new_items_count)} new items added to db")
        else:
            print("There is no items to add")
