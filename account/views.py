from email.message import Message
from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

from .forms import CreateUserForm,BatteryDetailsFrom
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    pass
    # return render(request,'dashboard.html')

#Registration
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was cretaed for' + user)
            return redirect('login') 
    context = {'form': form }
    return render(request, 'register.html', context)

#Login    
def loginPage(request):
	# if request.user.is_authenticated:
	# 	return redirect('home')
	# else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home') 
        else:
            return redirect('home')
            
    context = {}
    return render(request, 'login.html', context)

#Logout
def logoutUser(request):
	logout(request)
	return redirect('login')

def forgotPassword(request):
    pass


def batteryDetails(request):
    # fm = BatteryDetailsFrom()
    if request.method == 'POST':
        fm = BatteryDetailsFrom(request.POST)
        if fm.is_valid():
            fm.save()
        fm = BatteryDetailsFrom()
        # else:
        #     messages.info(request, "Unable to Submit Data")
    else:
        fm = BatteryDetailsFrom()
    context = {'submit_data': fm }
    return render(request,'dashboard.html', context)


def getBatteryDetails(request):
    if request.method == "GET":
        data = BatteryDetail.objects.values()
    
    context = {'battery_data': data }
    return render(request, 'battery_details.html',context)


def updateBattery(request):
    pass