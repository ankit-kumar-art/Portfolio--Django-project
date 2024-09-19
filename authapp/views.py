from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as ulogin, logout as ulogout

# Create your views here.
def login(request):
    if request.method=='POST':
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1') 
        myuser=authenticate(username=get_email,password=get_password) 
        if myuser is not None:
            ulogin(request,myuser)
            messages.success(request,"Login success")
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/auth/login/')  
            
    return render(request,'login.html')
   

def signup(request):
    if request.method=='POST':
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        get_confirm_password=request.POST.get('pass2')
        if get_password != get_confirm_password:
            messages.info(request,'Password is not matching')
            return redirect('/auth/signup/')
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,'email is taken')
                return redirect('/auth/signup/')
        except User.DoesNotExist:
            pass
        myuser=User.objects.create_user(get_email,get_email,get_password)
        myuser.save()
        messages.success(request,'User is created succesfully. please Login')
        return redirect('/auth/login/') 
    return render(request,'signup.html')

def logout(request):
    ulogout(request)  # Correctly log out the user
    messages.success(request, "Logged out successfully")
    # return redirect('/auth/login/')  # Redirect to login page after logout
    return render(request,'login.html')