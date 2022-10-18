from django.db import models
from datetime import datetime

from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    # Figure out TextField(blank=True)
    description = models.TextField(blank=True)

    price = models.IntegerField()
    bedrooms = models.IntegerField()
    # Figure out DecimalField(max_length=2)
    bathrooms = models.DecimalField(max_length=2)

    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    # Figure out DecimalField(max_digits=5, decimal_places=1)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)

    # Figure out (upload_to='photos/%Y/%m/%d/')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')

    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    # Figure out DateField(default=datetime.now(), blank=True)
    list_date: models.DateField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title

