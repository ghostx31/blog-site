from django.shortcuts import render, redirect
from .models import UserProfile

# Create your views here.
from django.urls import path

def userBlogs(request):
    return render(request, "user_blog.html")


def userFav(request):
    return render(request, "user_fav.html")

#def userProf(request):
    #return render(request, "user.html")

def SubmitBlog(request):


    return render(request, "user_blog.html")


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
    return render(request, "body.html")