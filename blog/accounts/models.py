from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
# Create your models here.

class UserLogin(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    login_count = models.PositiveIntegerField(default=0)

#python3 manage.py makemigrations
