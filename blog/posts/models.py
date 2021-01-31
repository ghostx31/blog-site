from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class BlogPost(models.Model):
        #title = models.CharField(max_length=30)
        editor = RichTextField()
        tags = models.CharField(max_length=25)


class UserProfile(models.Model):
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

