from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from listings.choices import bedroom_choices, price_choices, state_choices

from .models import Listing


# index page for the listings
def index(request):
  listings = Listing.listings.order_by('-list_date').filter(is_published = True)

  paginator = Paginator(listings, 6)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  context = {
    'listings': page_obj
  }
  return render(request, 'listings/listings.html', context)

# show one listing
def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  thumbnails = [
    listing.photo_1,
    listing.photo_2,
    listing.photo_3,
    listing.photo_4,
    listing.photo_5,
    listing.photo_6,
  ]
  # remove all the empty values
  thumbnails = list(filter(lambda x: x != '', thumbnails))

  context = {
    'listing': listing,
    'thumbnails': thumbnails,
  }
  return render(request, 'listings/listing.html', context)

# search for a listing
def search(request):
  query_set_list = Listing.listings.order_by('-list_date')

  # keywords
  if 'keywords' in request.GET and request.GET['keywords'] != '':
    keywords = request.GET['keywords']
    query_set_list = query_set_list.filter(description__icontains=keywords)

  # city
  if 'city' in request.GET and request.GET['city'] != '':
    city = request.GET['city']
    query_set_list = query_set_list.filter(city__iexact = city)

  # state
  if 'state' in request.GET:
    state = request.GET['state']
    query_set_list = query_set_list.filter(state__exact = state)

  # bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    query_set_list = query_set_list.filter(bedrooms=bedrooms)

  # price
  if 'price' in request.GET:
    price = request.GET['price']
    query_set_list = query_set_list.filter(price__lte = price)

  context = {
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'state_choices': state_choices,
    'listings': query_set_list,
    'values': request.GET,
  }
  return render(request, 'listings/search.html', context)