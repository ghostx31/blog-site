from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from homepage.models import feedbackModel, Uploads, Like
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from posts.models import UserProfile


from .models import BlogPost
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
# Create your views here.
def home(request):
    blogs = BlogPost.objects.all()
    print(blogs)
    return render(request, "index.html", {"blog":blogs})
   

def aboutus(request):
    user = User.objects.all()
    print(user)
   
    return render(request, 'aboutus.html', {"user" : user })

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
        #cat = BlogPost.objects.filter(id=request.user.id)


    print(blogs)
    return render(request, "user_blog.html", {'blog': blogs, 'user':user })




def blogDetail(request, slug):
    blog = BlogPost.objects.filter(author=request.user.id, slug=slug)

    return render(request, "blog.html", {"blog": blog })


def like_post(request):
    user = request.user

    if request.method == "POST":
        post_id =  request.POST.get("post_id")
        post_obj = BlogPost.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, id=post_id)

        if not created:
            if like.value == "Like":
                like.value = "Unlike"
            else:
                like.value = "like"

        like.save()
    return redirect('posts:Views')



def blogRead(request, slug):
    blog = BlogPost.objects.get(slug=slug)

    return render(request, "blogread.html", {"blog": blog })