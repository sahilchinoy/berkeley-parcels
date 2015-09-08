# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('APN', models.CharField(db_index=True, max_length=15)),
                ('condo', models.CharField(max_length=10)),
                ('point_x', models.FloatField()),
                ('point_y', models.FloatField()),
                ('locationid', models.FloatField()),
                ('streetnum', models.FloatField()),
                ('prequalifi', models.CharField(max_length=254)),
                ('direction', models.CharField(max_length=254)),
                ('streetname', models.CharField(max_length=254)),
                ('streetsuffix', models.CharField(max_length=254)),
                ('unit', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('state', models.CharField(max_length=254)),
                ('zip_code', models.CharField(max_length=254)),
                ('usecode', models.CharField(max_length=254)),
                ('usecodedes', models.CharField(max_length=254)),
                ('bldgsqft', models.FloatField()),
                ('lotsqft', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('x_min', models.FloatField()),
                ('x_max', models.FloatField()),
                ('y_min', models.FloatField()),
                ('y_max', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('shape_len', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('owner', models.CharField(null=True, max_length=200, blank=True)),
            ],
        ),
    ]
