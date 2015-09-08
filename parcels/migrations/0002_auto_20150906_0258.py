# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='parcel',
            name='building_size',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='parcel',
            name='county_use',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='parcel',
            name='lot_size',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='parcel',
            name='web_location_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
