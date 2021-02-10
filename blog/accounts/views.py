from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import UserLogin
from posts import views
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password1 = request.POST['password1']
        password2 = request.POST["password2"]
        email = request.POST["email"]
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken. ")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists. ")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("Saved")
        else:
            messages.info(request, "Passwords do not match. ")
        return redirect("/")
    else:
        print("No")
    return render(request, "register.html")

'''def LoginAuth(request):
    if person.objects.get(last_login) == NULL:
        return render(request, "user.html")
    else:
     return render(request, "body.html")



def LoginAuth(request):
    if UserLogin.objects.only(login_count) == 0 or UserLogin.objects.only(login_count) == 1:
        UserFirst()

    else:
        login()


def LoginAuth(request):
    UserLogin.objects.only("login_count")
    if login_count == 0 or login_count == 1:
        posts.UserFirst()
    else:
        post.UserNormal()

'''
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)



        if user is not None:
            name = User.objects.get(username=username)
            last_login = name.last_login
            print(last_login)
            login(request, user)
            if last_login == None:
                return redirect("/user/first/")
            else:
                return redirect("/user/profile/")
        else:
            print("No")
            messages.info(request, "Invalid credentials ")

            return redirect("/")

    else:
        print("Ok")
        return render(request, "log-in-up.html")


def logout_view(request):
    auth.logout(request)
    return redirect("/")