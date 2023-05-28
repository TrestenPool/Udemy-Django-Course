from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render

from contacts.models import Contact


##################
#### Login ######
##################
def login(request):

  # GET request
  if request.method == 'GET':
    return render(request, 'accounts/login.html')

  # POST request
  elif request.method == 'POST':
    # get the user input
    username = request.POST['username']
    password = request.POST['password']

    # Checks to see if the username and password matches in the db
    user = auth.authenticate(username=username, password=password)

    # the user was not found, redirect to the login page again
    if user is None:
      messages.error(request, 'username or password is incorrect')
      return redirect('login')

    # the user was found, log them in and redirect to the index page
    messages.success(request, 'You have successfully logged in!')
    auth.login(request, user)
    return redirect('index')

  # Bad request
  else:
    return HttpResponseBadRequest(f'This route does not allow the {request.method} method.')
    
##################
#### Register ####
##################
def register(request):
  # GET Request
  if request.method == 'GET':
    return render(request, 'accounts/register.html')

  # POST Request
  elif request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    anyError = False

    ### Checks for the following error ###
    # password does not match
    if password != password2:
      messages.error(request, 'The confirmation password does not match')
      anyError = True
    # username already exists
    if User.objects.filter(username=username).exists():
      messages.error(request, f'The username {username} is already taken, please select another')
      anyError = True
    # Checks if the email already exists
    if User.objects.filter(email=email).exists():
      messages.error(request, f'The email {email} is already taken, please select another')
      anyError = True
    
    # if there are any errors, return to the register screen with the errors
    if anyError:
      return redirect('register')
    # There was no errors, so go ahead and proceed
    else:
      new_user = User.objects.create(username=username, password=password, email=email,
                                     first_name=first_name, last_name=last_name)
      auth.login(request, new_user)
      messages.success(request, 'You have successfully register and logged in')
      return redirect('index')
      
  # Bad Request
  else:
    return HttpResponseBadRequest(f'This route does not allow the {request.method} method.')

##################
#### Logout ####
##################
def logout(request):
  # check if the user is authenticated and log them out if they are 
  if request.user.is_authenticated:
    auth.logout(request)
    messages.success(request,  "You have successfully logged out")
    return redirect('index')
  # There was no user logged in, tell them can't logout because there was nobody that was logged in the first place
  else:
    messages.warning(request,  "Unable to logout because nobody was logged in, in the first place")
    return redirect('index')
    

##################
#### Dashboard ####
##################
def dashboard(request):
  # gets all of the contacts made by the user that is logged in
  user_contacts = Contact.objects.order_by('contact_date').filter(user_id=request.user.id)

  context = {
    'contacts': user_contacts
  }

  return render(request, 'accounts/dashboard.html', context)
