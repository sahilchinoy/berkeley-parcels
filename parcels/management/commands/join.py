import os
import csv

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction

from parcels.models import Parcel

class Command(BaseCommand):

    def handle(self, *args, **options):
        path = os.path.join(
            settings.DATA_DIR, 'scraped_parcels.csv')

        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                parcel = Parcel.objects.get(APN=row['APN'])
                owner = row['owner'].replace('&amp;','&')
                print(owner)
                parcel.owner = owner
                parcel.address = row['address']
                parcel.lot_size = row['lot_size']
                parcel.building_size = row['building_size']
                parcel.county_use = row['county_use']
                parcel.web_location_id = row['location_id']
                parcel.save()