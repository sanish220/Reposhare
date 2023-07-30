from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.forms import customform

# Create your views here.

def register(request):
    if request.method =='POST':
        form = customform(request.POST)
        for data in form:
            print(data,data.label)
        if form.is_valid():
            form.save()
            return redirect(log_in)
        else:
            return HttpResponse('form invalid')
    else:
        form = customform()
    return render(request,'register.html',{'form':form})

def log_in(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user =authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect(dashboard)
    return render(request,'login.html')

def dashboard(request):

    return render(request,'dashboard.html')