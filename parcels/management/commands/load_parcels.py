import os

from django.conf import settings
from django.db import transaction
from django.core.management.base import BaseCommand
from django.contrib.gis.gdal import SpatialReference
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource

from parcels.models import Parcel


class Command(BaseCommand):
    help = "Load parcels from shapefile."

    def handle(self, *args, **options):
        Parcel.objects.all().delete()
        path = os.path.join(
            settings.DATA_DIR,
            'Parcels',
            'Parcels.shp')

        parcel_mapping = {
            'APN' : 'APN',
            'condo' : 'CONDO',
            'point_x' : 'POINT_X',
            'point_y' : 'POINT_Y',
            'locationid' : 'LocationID',
            'streetnum' : 'StreetNum',
            'prequalifi' : 'Prequalifi',
            'direction' : 'Direction',
            'streetname' : 'StreetName',
            'streetsuffix' : 'StreetSufx',
            'unit' : 'Unit',
            'city' : 'City',
            'state' : 'State',
            'zip_code' : 'Zip',
            'usecode' : 'UseCode',
            'usecodedes' : 'UseCodeDes',
            'bldgsqft' : 'BldgSqft',
            'lotsqft' : 'LotSqft',
            'latitude' : 'latitude',
            'longitude' : 'longitude',
            'x_min' : 'X_min',
            'x_max' : 'X_max',
            'y_min' : 'Y_min',
            'y_max' : 'Y_max',
            'shape_area' : 'Shape_area',
            'shape_len' : 'Shape_len',
            'geom' : 'MULTIPOLYGON',
        }

        lm = LayerMapping(
            Parcel,
            path,
            parcel_mapping,
            source_srs=SpatialReference(32610))
        lm.save(verbose=True)
