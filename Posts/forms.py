from django import forms
from . models import POST,Comments

class PostForm(forms.ModelForm):
    class Meta:
        model=POST
        fields=['Title','image_post','files','caption']


class Createcommentform(forms.ModelForm):
    class Meta:
        model=Comments
        
        fields=['comm']