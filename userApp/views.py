from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post

# Create your views here.

def index(request):
    my_user = UserAuthentication()
    form = {'form': my_user}
    return render(request, 'index.html', form)

def register(request):
    return render(request, 'register.html')


def register_form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        return redirect('/')
    else:
        return HttpResponse('User could not be registered. Try again!')


def login_user(request):
    if request.method == 'POST':
        login_username = request.POST['username']
        login_password = request.POST['password']

        user = authenticate(username=login_username, password =login_password)

        if user is not None:
            login(request, user)
            messages.success(request, 'User Logged In!')
            return redirect('/')
        else:
            return HttpResponse('Invalid credentials. Register first to login!')

def logout_user(request):
    logout(request)
    messages.success(request, 'User Logged Out!')
    return redirect('/')

def create_post(request):
    if request.method == 'POST':
        p = Post()
        p.user = request.user
        p.text = request.POST.get('posttext')
        p.save()
        messages.info(request, 'Posted successfully!')
        return redirect('/') 
    else:
        return HttpResponse('Post could not be created. Try again.')