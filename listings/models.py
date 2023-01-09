from datetime import datetime

from django.db import models
from django.db.models import Avg
from realtors.models import Realtor


# Listing model
class Listing(models.Model):
  listings = models.Manager()
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
  garage = models.IntegerField(default=0) 
  sqft = models.IntegerField() 
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  photo_main = models.ImageField(upload_to='images/%m/%d/%Y/')
  photo_1 = models.ImageField(upload_to='images/%m/%d/%Y/', blank=True)
  photo_2 = models.ImageField(upload_to='images/%m/%d/%Y/', blank=True)
  photo_3 = models.ImageField(upload_to='images/%m/%d/%Y/', blank=True)
  photo_4 = models.ImageField(upload_to='images/%m/%d/%Y/', blank=True)
  photo_5 = models.ImageField(upload_to='images/%m/%d/%Y/', blank=True)
  photo_6 = models.ImageField(upload_to='images/%m/%d/%Y/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.title

# go back to this, 
# class AverageListings(models.Manager):
#   def avg_listing_price(self):
#     return self.annotate(avg_price=Avg('price'))