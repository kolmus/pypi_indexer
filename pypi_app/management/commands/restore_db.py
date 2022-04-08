from django.core.management.base import BaseCommand

import tarfile
import glob
import os
import json

from pypi_app.models import Item
from pypi_indexer.settings import ARCHIVE_DIRECTORY


class Command(BaseCommand):
    """
    This script restores database from latest archive tar.bz2 file.
    Update or creates new data
    """
    def handle(self, *args, **options):
        
        path = f'{ARCHIVE_DIRECTORY}/*.tar.bz2'

        files = glob.glob(path)
        last_file = max(files, key=os.path.getctime)
        unpacked = tarfile.open(last_file)
        unpacked.extract('data.json', ARCHIVE_DIRECTORY)
        
        updated_objects = 0
        data = json.load(open(ARCHIVE_DIRECTORY + '/data.json'))
        for model in data:
            
            if model['model'] == "pypi_app.item":
                fields = model['fields']
                
                updated = Item.objects.update_or_create(
                    id=model['pk'],
                    title=fields['title'],
                    version=fields['version'],
                    link=fields['link'],
                    guid=fields['guid'],
                    description=fields['description'],
                    author_name=fields['author_name'],
                    author_email=fields['author_email'],
                    pub_date=fields['pub_date']
                )
                if updated[1] == True:
                    updated_objects += 1
        os.remove(ARCHIVE_DIRECTORY + '/data.json')
        if updated_objects:
            print(f'\nOdtworzono {updated_objects} rekordów!\n')
        else: print('\nNie odtworzono żadnego rekordu!\n')