from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .models import Listing


# index page for the listings
def index(request):
  listings = Listing.listings.all()

  paginator = Paginator(listings, 3)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  context = {
    'listings': page_obj
  }
  return render(request, 'listings/listings.html', context)

# show one listing
def listing(request, listing_id):
  return render(request, 'listings/listing.html')

# search for a listing
def search(request):
  return render(request, 'listings/search.html')