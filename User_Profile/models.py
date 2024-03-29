from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
 
from django.dispatch import receiver

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Bio=models.TextField()
    Work_links=models.URLField()
    image=models.ImageField(default='default.jpg',upload_to='profile_images')
    def __str__(self):
        return f'{self.user} Profile '


@receiver(post_save,sender=User)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile.objects.create(user=kwargs['instance'])
       
@receiver(post_save,sender=User)

def save_profile(sender,instance, **kwargs):
    instance.profile.save()





   
        
   