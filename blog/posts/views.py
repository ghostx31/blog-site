from django.shortcuts import render, redirect

#from blog.homepage.models import BlogPost
from .models import UserProfile
from django.contrib.auth.models import User
# Create your views here.
from django.urls import path
from homepage.models import BlogPost 
from posts.models import UserProfile 


def blogCat(request):
    cat = BlogPost.objects.all()
    print(cat)
    return render(request, "user_fav.html",  {"cat" : cat })


def fav(request):
    return render(request, "user_fav.html")


def UserFirst(request):
    if request.method == "POST":    
    
        image = request.FILES.get('image')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        linkedin = request.POST.get("linkedin")
        instagram = request.POST.get("instagram")
        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
        hobby  = request.POST.get("hobby")
        subject = request.POST.get("subject")
        ins = UserProfile(firstname=firstname, lastname=lastname, email=email, linkedin=linkedin, instagram=instagram, twitter=twitter, facebook=facebook, hobby=hobby, subject=subject)
        ins.save()
        print("Yes")
        return redirect("/")
    else:
        print("No")

    return render(request, "user.html")

def UserNormal(request):
    data = UserProfile.objects.get(id=request.user.id)
    print(data)
    return render(request, "user_profile.html", {"data":data })






