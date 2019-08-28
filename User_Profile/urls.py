from django.contrib import admin
from django.urls import include, path
from . import views


from django.contrib.auth import views as auth_views

urlpatterns = [

    path('profile', views.profil,name='profil'),
    path('edit',views.edit_profile,name='edit_profile')
    
]

