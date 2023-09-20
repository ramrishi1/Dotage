from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserChangeForm
from user.models import *
from .models import Profile
from .models import Event
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.contrib import messages


def loginpage(request):
    return render(request, 'BeforeLogin/login.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url=loginpage)
def events(request):
    return render(request, 'AfterLogin/events.html')

@login_required(login_url=loginpage)
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users':users})

@login_required(login_url=loginpage)
def usersafterlogin(request):
    users = User.objects.all()
    return render(request, 'AfterLogin/usersafterlogin.html', {'users':users})

def signupage(request):
    return render(request, 'signup/signup.html')

@login_required(login_url=loginpage)
def eventcreation(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        event_desc = request.POST['event_desc']
        event_address = request.POST['event_address']
        event_city = request.POST['event_city']
        event_date = request.POST['event_date']
        event_zip = request.POST['event_zip']

        user = request.user

        event_image = request.FILES['event_image']

        # event = Event(
        #     uid=user,
        #     ename=event_name,
        #     edesc=event_desc,
        #     eaddress=event_address,
        #     ecity=event_city,
        #     edate=event_date,
        #     ezip=event_zip,
        #     image=event_image
        # )
        if event_image:
            event = Event(
                uid=user,
                ename=event_name,
                edesc=event_desc,
                eaddress=event_address,
                ecity=event_city,
                edate=event_date,
                ezip=event_zip,
                image=event_image
            )
        else:
            # Create an event without an image
            event = Event(
                uid=user,
                ename=event_name,
                edesc=event_desc,
                eaddress=event_address,
                ecity=event_city,
                edate=event_date,
                ezip=event_zip
            )
        event.save()
        print("Success")
        return redirect('eventcreation')
    return render(request, 'eventcreation/eventcreation.html')


@login_required(login_url=loginpage)
def afterlogin(request):
    return render(request, 'AfterLogin/afterlogin.html')


def eventslogin(request):
    return render(request, 'AfterLogin/eventslogin.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            if User.objects.filter(username=username):
                print('User already exists')
                return redirect(signupage)
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                return redirect(registerpage, id=user.id)
        else:
            print('Invalid Password')
            return redirect(signupage)
       


def registerpage(request, id):
    user = User.objects.get(id=id)
    return render(request, 'signup/register.html', {'userdata': user})


def register(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        dob = request.POST['dob']
        phonenumber = request.POST['phonenumber']
        postcode = request.POST['postcode']
        profile = Profile(uid=user, dob=dob, phonenumber=phonenumber, postcode=postcode)
        profile.save()
        return redirect(loginpage)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginuser = auth.authenticate(username=username, password=password)
        if loginuser is not None:
            auth.login(request, loginuser)
            return redirect(afterlogin)
        else:
            return redirect(loginpage)
    else:
        return redirect(loginpage)

def logout(request):
    auth.logout(request)
    return redirect(loginpage)

@login_required
def profile(request):
    user_profile = Profile.objects.get(uid=request.user)
    users = User.objects.all()
    if request.method == 'POST':
        profile_image = request.FILES['profile_image']
        user_profile.image = profile_image
        user_profile.save()
        return redirect('profile')
    return render(request, 'AfterLogin/profile.html', {'user_profile': user_profile,'users':users})

def editprofile(request):
    if request.method=='POST':
        form=UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('AfterLogin/profile.html')
        
def eventsafterlogin(request):
    events = Event.objects.select_related('uid').all()
    return render(request, 'AfterLogin/eventsafterlogin.html', {'events': events})

def eventdetails(request, event_id):
    events = Event.objects.get(id=event_id)
    return render(request, 'eventdetails.html', {'event': events})