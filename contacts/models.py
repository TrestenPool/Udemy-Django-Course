from datetime import datetime

from django.db import models


class Contact(models.Model):
  # name of the listing the inquiry is about
  listing = models.CharField(max_length=255)
  # if of the listing the inquiry is about
  listing_id = models.IntegerField()
  
  # information aquired from the person who made the inquiry
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  
  # Optional fields, allowed to be left blank
  message = models.TextField(max_length=255, blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  
  def __str__(self):
    return self.name
 