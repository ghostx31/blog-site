from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.timezone import now
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
    opt = [
        ("Technology", "Technology"),
        ('Mathematics', "Mathematics"),
        ("Social Media", "Social Media")
    ]
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    editor = RichTextField()
    topic = models.CharField(choices=opt, max_length=25)
    time = models.DateField(default=now)
    slug = models.CharField(max_length=130)

    def __str__(self):
        return self.title + '|' + str(self.author)
