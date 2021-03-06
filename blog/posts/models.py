from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserProfile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    filename = models.FileField(upload_to="UserPics")
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    email = models.EmailField(max_length=40)
    linkedin = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    twitter = models.URLField(max_length=220)
    facebook = models.URLField(max_length=220)
    hobby = models.CharField(max_length=100)
    subject = models.TextField()


