from django.shortcuts import render,redirect
from django.contrib import messages
from .form import RegistrationForm
from django.contrib.auth import authenticate,login
# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successful")
            return redirect("registration")
        messages.error(request,form.errors)
        return redirect("registration")
    
    else:
        form=RegistrationForm()
        context={
            "form": form    
        }
        return render (request,"registration.html",context)   
    
def signin(request) :
    if request.method=="POST":
        Username=request.POST.get("username")
        Password=request.POST.get("password")
        user=authenticate(request,username=Username,password=Password)
        if user is not None:
            login(request,user)
            return redirect ("home")
        messages.error(request,"Invalid username or password")
        return redirect ("signin")
    return render (request,"login.html")