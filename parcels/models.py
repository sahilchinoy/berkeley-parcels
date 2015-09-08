from django.contrib.gis.db import models

class Parcel(models.Model):
    APN = models.CharField(max_length=15, db_index=True)
    condo = models.CharField(max_length=10)
    point_x = models.FloatField()
    point_y = models.FloatField()
    locationid = models.FloatField()
    streetnum = models.FloatField()
    prequalifi = models.CharField(max_length=254)
    direction = models.CharField(max_length=254)
    streetname = models.CharField(max_length=254)
    streetsuffix = models.CharField(max_length=254)
    unit = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=254)
    zip_code = models.CharField(max_length=254)
    usecode = models.CharField(max_length=254)
    usecodedes = models.CharField(max_length=254)
    bldgsqft = models.FloatField()
    lotsqft = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    x_min = models.FloatField()
    x_max = models.FloatField()
    y_min = models.FloatField()
    y_max = models.FloatField()
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    owner = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    lot_size = models.FloatField(null=True)
    building_size = models.FloatField(null=True)
    county_use = models.CharField(max_length=200, null=True, blank=True)
    web_location_id = models.CharField(max_length=10, null=True, blank=True)

    objects = models.GeoManager()

    class Meta:
        ordering = ['lot_size']

    def __str__(self):
        return self.address
