from django.contrib import admin
from parcels.models import Parcel

class ParcelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Parcel, ParcelAdmin)