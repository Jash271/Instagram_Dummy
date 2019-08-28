from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=100)
    Last_name=forms.CharField(max_length=100)

    class meta:
        model=User
        fields=['email','first_name','Last_name','password1','password2']


    def save(self,commit=True):
        User=super(UserRegistrationForm,self).save(commit=False)
        User.first_name=self.cleaned_data['first_name']
        User.last_name=self.cleaned_data['Last_name']
        User.email=self.cleaned_data['email']

        if commit:
            User.save()

        
           
