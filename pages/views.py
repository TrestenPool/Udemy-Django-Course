from django.http import HttpResponse
from django.shortcuts import render

# Models
from listings.models import Listing
from realtors.models import Realtor

from listings.choices import bedroom_choices, price_choices, state_choices


# Create your views here.
def index(request):
  listings = Listing.listings.order_by('-list_date').filter(is_published=True)[:3]
  num_listings = listings.count()
  context = {
    'listings': listings,
    'num_listings': num_listings,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'state_choices': state_choices,
  }
  return render(request, 'pages/index.html', context)

def about(request):
  realtors = Realtor.realtors.order_by('-hire_date')
  realtor_of_the_month = Realtor.realtors.filter(is_mvp=True)
  realtor_of_the_month = realtor_of_the_month[0] if realtor_of_the_month.exists() else None
    
  context = {
    'realtors': realtors,
    'realtor_of_the_month': realtor_of_the_month
  }
  return render(request, 'pages/about.html', context)
