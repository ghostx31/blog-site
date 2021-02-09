from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'posts'
urlpatterns = [
    path('', views.home, name='home-page'),
    path('about/', views.aboutus, name='about-us'),
    path('contact/', views.contact, name='contact'),
    path('create/', views.create, name='create'),
    #path('profile/', views.profile, name='profile'),
    #path('login/', views.login, name='login'),
    path('search/',  views.search, name='search'),
    path('myblogs/', views.ViewBlogs, name="Views"),
    path('myblogs/<slug:slug>', views.blogDetail, name='detail'),
    path('like/', views.like_post, name='like-post'),

]