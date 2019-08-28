from django.shortcuts import render
from . forms import PostForm,Createcommentform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from  django.contrib.auth.models import User
import pdb
from django.views.generic import ListView,DetailView,CreateView
from . models import POST,Comments
from datetime import datetime


# Create your views here.
@login_required
def my_post(request):
    val1=models.POST.objects.filter(id=request.user.id)
    val2=request.user.username
    val3=models.Comments.objects.filter(comment_id__in=val1)
    

    return render(request,"my_post.html",{'val1':val1,'val2':val2,'val3':val3})


class PostListView(ListView):
    model=POST
    template_name="postquery.html"
    context_object_name='val1'
    
    ordering=['-dateposted']
    
    def get_queryset(self):
        return POST.objects.filter(author=self.request.user)




class PostDetailView(DetailView):
    model=  POST
    template_name="postquery1.html"


def comment_view(request,obj_id):
    
    
    val3=models.Comments.objects.filter(comment_id=obj_id)
    return render(request,"postquery2.html",{'val3':val3})


class PostCreateView(CreateView):
    model=POST
    form_class=PostForm
    template_name="CreatePost.html"

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


def createcomment(request,obj_id):
    val1=obj_id
    request.session['val2']=val1
    
    return render(request,"Create_comment.html",{'val1':val1})
    
    



def created(request):
    comment=models.Comments()
    x=request.POST['comment']
    
    comment.comm=x
    comment.author_comment=request.user
    
    
    comment.comment_id=request.POST['number']
    comment.save()
    return render(request,"postquery.html")
   








   
