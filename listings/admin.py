from django.contrib import admin
from .models import Listing

# add the Listing model to login into the admin site
admin.site.register(Listing)
