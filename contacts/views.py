from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Contact


def contact(request):
  # POST request
  if request.method == 'POST':
    
    # Get the variables from the post request body
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, "You have already made and inquiry for this listing!!")
        return redirect('/listings/' + listing_id)

    # Create the contact object
    contact = Contact(listing=listing, listing_id = listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

    # Save the object in the db 
    contact.save()

    # send email
    send_mail(
      subject='There has been an inquiry for the listing ' + listing,
      message=message,
      from_email="trestenpool@gmail.com",
      recipient_list=[realtor_email, 'trestenpool@gmail.com'],
      fail_silently=False
    )

    # Setup the flash message, redirect the user back to the same listing page
    messages.success(request, "Succesfully submited your inquiry")
    return redirect('/listings/'+listing_id)

  # GET request
  elif request.method == 'GET':
    return HttpResponse('get request submitted to /contact')

  # Unsupported request method
  else:
    return 'method not supported'
