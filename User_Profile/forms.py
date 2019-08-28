from django import forms
from . models import profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

   


class ProfileUpdateForm(forms.ModelForm):
    Work_links=forms.URLField(required=False)
    class Meta:
        model=profile
        fields=['Bio','image','Work_links']
    
