from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=100)

    
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='notes', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    image= models.ImageField(upload_to='images/' ,null=True, blank=True) 


    def __str__(self):
        return "({}) - {}".format(self.user, self.title)
