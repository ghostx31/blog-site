from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
class feedbackModel(models.Model):
    opt = [
        ("Comments", "Comments"),
        ("Suggestions", "Suggestions"),
        ("Questions", "Questions")
    ]
    FeedbackType = models.CharField(choices=opt, max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.TextField()



class Uploads(models.Model):
    BlogData = models.TextField()

class BlogPost(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    editor = RichTextField()
    topic = models.CharField(max_length=25)