from django.shortcuts import render
from . forms import UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import  profile
from  django.contrib.auth.models import User

# Create your views here.
@login_required
def profil(request):
    
    return render(request,"profile.html")

@login_required
def edit_profile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return render(request,"profile.html",{'p_form':p_form})
    else:
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)


    return render(request,"Edit_Profile.html",{'u_form':u_form,'p_form':p_form})




