from django.contrib import admin
from .models import BlogPost, UserProfile
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(UserProfile)