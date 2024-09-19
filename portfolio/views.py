from django.shortcuts import render, redirect
from django.contrib import messages
from .models import contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    if request.method == 'POST':                           
        fname = request.POST.get('name') # Changed 'name' to 'fname' to match your form field
        femail = request.POST.get('email')
        fphone = request.POST.get('phone')
        fdesc = request.POST.get('desc')
        
        
        query=contact(name=fname,email=femail,phonenumber=fphone,description=fdesc) 
        query.save()

        #Display a message with the information
        #messages.info(request, f'The name is {fname}, email is {femail}, phone {fphone}, description {fdesc}')

        # Create an instance of the contact model
        
        #query.save()
        #print("data is comming")
        #print(fname,femail,fphone,fdesc)
        # Display a success message
        messages.success(request, 'Thanks for contacting us. We will get back to you soon.')
        return redirect('/contact')

    return render(request, 'contact.html')

def resume(request):
    return render(request, 'resume.html')

def project(request):
    return render(request, 'project.html')
