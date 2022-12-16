from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def home(request):
    return render(request,'home.html')
@cache_page(60*15)
@csrf_protect
def login(request):
     if request.method=="POST":
        username = request.POST.get('user','')
        password = request.POST.get('pass','')
        print(username,password)
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            login(request,user)
            return render(request,'upload.html')

          # A backend authenticated the credentials
        else:
            return render(request,'login.html')
            # No backend authenticated the credentials
    
     

     return render(request,'login.html')
    


def upload(request):
    return render(request,'upload.html')

def result(request):
    return render(request,'result.html')


