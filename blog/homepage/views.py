from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from homepage.models import feedbackModel, Uploads
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.utils import timezone

from .models import BlogPost
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    if request.method == "POST":
        feedback = request.POST.get("FeedbackType")
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        email = request.POST.get("email")
        sub = request.POST.get("subject")
        print("yes")
        print(feedback, fname, lname, email, sub)
        try:
            validate_email(email)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            print("Valid email. ")
        ins = feedbackModel(FeedbackType=feedback, firstname=fname, lastname=lname, email=email, subject=sub)
        ins.save()
    else:
        print("No")
    return render(request, 'contactus.html')

def create(request):
    if request.method == "POST":

        title = request.POST.get('title')
        editor = request.POST.get('editor')
        topic = request.POST.get('topic')
        time = request.POST.get('time')
        print(editor)
        print("Yes")

        BlogIns = BlogPost(title=title, topic=topic, editor=editor)
        BlogIns.author = request.user
        BlogIns.save()

    else:
        print("No")
    return render(request, 'create_new.html')

def login(request):

    return render(request, 'log-in-up.html')
def profile(request):
    return render(request, "user.html")


def search(request):
    query = request.GET['query']
    #allposts = BlogPost.objects.all()
    allposts = BlogPost.objects.filter(title__icontains=query)

    params = {'allposts': allposts}
    return render(request, 'searchpage.html', params)
    #return HttpResponse("This is a search. ")



def ViewBlogs(request):
    if request.user.is_authenticated:
        print("Yess")
        user = request.user.username
        print(user)
        num_post = BlogPost.objects.filter(author=request.user.id).count()
        print(num_post)
        blogs = BlogPost.objects.filter(author=request.user.id)

        print("output", blogs)


    print(blogs)
    return render(request, "user_blog.html", {'blog': blogs, 'user':user })


def AllBlogs(request, id):
    blogs = BlogPost.objects.all()
    return render(request, "index.html", {"blog":blogs})


def blog_detail(request, slug):
    return HttpResponse(slug)