from django.contrib import admin
from django.urls import include, path
from django.conf import settings 
from django.conf.urls.static import static
from . import views
from . views  import PostListView,PostDetailView,PostCreateView
from django.contrib.auth import views as auth_views
app_name="Posts"

urlpatterns = [

   
    path('post_view',PostListView.as_view(),name='post_view'),
    path('post_detail/<int:pk>',PostDetailView.as_view(),name='post_detail'),
    path('comment_view/<obj_id>/',views.comment_view,name='comment_view'),
    path('post_create',PostCreateView.as_view(),name='create-post'),
    path('createcomment/<obj_id>/',views.createcomment,name='comment_create'),
    path('created',views.created,name='created'),
     
   
]

