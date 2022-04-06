from django.core.management.base import BaseCommand
from pypi_app.models import Item


class Command(BaseCommand):
    def handle(self, *args, **options):
        
        new_items = []
        
        # TODO Import, 
        # TODO mapping, 
        # TODO checking if item already exists, 
        # TODO backup db, 
        
        if new_items:
            new_items_count = Item.objects.bulk_create(new_items, ignore_conflicts=True)
            print(f'New {new_items_count} new items added to db')
        else:
            print("There is no items to add")
