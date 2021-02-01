from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from homepage.models import feedbackModel, Uploads
from django.contrib.auth.models import User
from .models import BlogPost

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
        print(editor)
        print("Yes")
        BlogIns = BlogPost(title=title, topic=topic, editor=editor)
        BlogIns.save()

    else:
        print("No")
    return render(request, 'create_new.html')

def login(request):

    return render(request, 'log-in-up.html')
def profile(request):
    return render(request, "user.html")


def search(request):
    return render(request, 'searchpage.html')
    #return HttpResponse("This is a search. ")

'''def blogs(request):
    if request.method == "POST":
        data = request.POST.get("editor")
        blogIns = Uploads(editor=data)
        blogIns.save()
        return render(request, "user_blog.html")
'''

