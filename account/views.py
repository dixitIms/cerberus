from email.message import Message
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

from .forms import BatteryDetailsFrom
from .models import *
from django.contrib import messages
from django.contrib.auth import logout
# from django.contrib.auth.models import User
import psycopg2 as db

uname=''
em=''
con=''
pwd=''
pwd_con=''


#REGISTER
def register(request):
    global uname,em,con,pwd,pwd_con
    if request.method=="POST":
        conn=db.connect(host="localhost",user="postgres",password="1234",database='battery_management')
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                uname=value
            if key=="email":
                em=value
            if key=="contact":
                con=value
            if key=="password":
                pwd=value
            if key=="password_conformation":
                pwd_con=value
        
        c="INSERT INTO account_crmuser Values('{}','{}','{}','{}','{}')".format(uname,em,con,pwd,pwd_con)
        cursor.execute(c)
        conn.commit()
        return redirect('login')

    return render(request,'register.html')

em=''
pwd=''
#Login
def loginPage(request):
    global em,pwd
    if request.method=="POST":
        m=db.connect(host="localhost",user="postgres",password="1234",database='battery_management')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from account_crmuser where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        print(t, "======>>>>>>")
        if t == ():
            messages.info(request, "Username or Password Inccorect")
        else:
            return redirect('home')

    return render(request,'login.html')

#Logout
def logoutUser(request):
    logout(request)
    return redirect('login')

def forgotPassword(request):
    pass

#Add_Battery_details
def batteryDetails(request):
    if request.method == "POST":
        fm = BatteryDetailsFrom(request.POST)
        print("Here======>>>>>")
        if fm.is_valid():
            fm.save()
            fm = BatteryDetailsFrom()
    else:
        print("ELSE HERE")
        fm = BatteryDetailsFrom()
    context = {'submit_data': fm }
    return render(request,'dashboard.html', context)

#Get_Battery_details
def getBatteryDetails(request):
    if request.method == "GET":
        data = BatteryDetail.objects.values()
    context = {'battery_data': data }
    return render(request, 'battery_details.html',context)

#This Function Will Update_Battery_details/Edit
def updateBatteryDetails(request, id):
    if request.method == 'POST':
        pi = BatteryDetail.objects.get(pk=id)
        fm = BatteryDetailsFrom(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = BatteryDetail.objects.get(pk=id)
        fm = BatteryDetailsFrom(instance=pi)
    return render(request,'update_battery_details.html',{'form': fm})
    

#Delete_Record
def deleteRecord(request,id):
    if request.method == 'POST':
        pi = BatteryDetail.objects.get(pk=id)
        pi.delete()
        return redirect('data')