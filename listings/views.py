from django.http import HttpResponse
from django.shortcuts import render


# index page for the listings
def index(request):
  return render(request, 'listings/listings.html')

# show one listing
def listing(request):
  return render(request, 'listings/listing.html')

# search for a listing
def search(request):
  return render(request, 'listings/search.html')