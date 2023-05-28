from django.urls import path

from . import views

urlpatterns = [
  # there are 2 ways to get to the index page
  path('', views.index, name='index'), 
  path('index', views.index, name='index'), 

  path('about', views.about, name='about'),
]