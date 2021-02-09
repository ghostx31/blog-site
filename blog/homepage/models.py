from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.text import slugify
from django.db.models.signals import pre_save
from blog.utils import unique_slug_generator
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
    title = models.CharField(max_length=100)
    editor = RichTextField()
    topic = models.CharField(choices=opt, max_length=25, null=True)
    time = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=130, null=True, blank=True)
    liked = models.ManyToManyField(User, related_name='liked')

    def __str__(self):
        return self.title + '|' + str(self.author)

    @property
    def num_likes(self):
        return self.liked.all().count()
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=BlogPost)



class Like(models.Model):
    Like_choices = (
        ("Like", "Like"),
        ("Unlike", "Unlike")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True)
    value = models.CharField(choices=Like_choices, default="Like", max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.post)