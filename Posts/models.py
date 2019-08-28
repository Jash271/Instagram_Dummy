
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.

class POST(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    Title=models.CharField(max_length=100,null=True)
    image_post=models.ImageField(upload_to='post_images',null=True)
    files=models.FileField(upload_to='myFiles',null=True)
    caption=models.TextField(null=True)
    dateposted=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.author} Post'


    



class Comments(models.Model):
    author_comment=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Title_comment=models.CharField(max_length=100,null=True)
    comment_id=models.ForeignKey(POST,on_delete=models.CASCADE,null=True)
    comm=models.TextField()
    date_commented=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.author_comment} comment'

