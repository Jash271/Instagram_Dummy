from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegistrationForm
from django.contrib import messages


# Create your views here.
def register(request):

    if request.method=='POST':
        form=UserRegistrationForm(request.POST)

        
        if form.is_valid():
           
            form.save()
            username=form.cleaned_data.get('username')
            
        
            messages.success(request,f"Account Created for {username}")
            return render (request,"home.html",{'user':request.user})
            
    else:
        form=UserRegistrationForm()
    return render (request,"register.html",{'form':form})


def home(request):
    return render(request,"home.html")