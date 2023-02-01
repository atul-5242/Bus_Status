from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from signup_student.models import StudentDetails
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
# import requests module
# import requests
from requests.auth import HTTPBasicAuth
import os
# os.path.join("D:/Project_Learning/Bus_Status/signup_student")
# from signup_student.models import StudentDetails
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User

from django.contrib import messages
# from django.http import HttpResponse
# Making a get request
# print request object

def homepage(request):
    return render(request,"Homepage.html")
# def login_details(request):
#     if request.method=="POST":
#         LoginID=request.POST["Id"]
#         LoginPassword=request.POST["password"]
#         print(LoginID)
#         print(LoginPassword)
        
        
#         user=authenticate(username=LoginID,password=LoginPassword)
        
        
#         if user is not None:
#             print("Yes")
#         else:
#             print("No")
#         if user is not None:
#             login(request,user)
#             # messages.success(request,"Successfully Logedin")
#             return redirect('home')
#         else:
#             return HttpResponse("Not logged In.")
           
#     return render(request,"login.html")
# def logout(request):
    
#     return redirect("Bus_Status/Logout")
def signup(request):
    if request.method=="POST":
        ID=request.POST.get("Id")
        Password1=request.POST.get("password1")
        Password2=request.POST.get("password2")
        # name=request.POST.get("fullname")
        email=request.POST.get("email")
        # print(email)
        # print(ID)
        # print(Password)
        # print(name)
        # print(email)
        data=StudentDetails(email=email,Id=ID,password1=Password1,password2=Password2)
        data.save() 
    return render(request,"signup.html")
# def infromation_inserting(request):
#     return render(request,"for_entring_information.html")