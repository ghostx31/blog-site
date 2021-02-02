from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about/', views.aboutus, name='about-us'),
    path('contact/', views.contact, name='contact'),
    path('create/', views.create, name='create'),
    #path('profile/', views.profile, name='profile'),
    #path('login/', views.login, name='login'),
    path('search/',  views.search, name='search'),

]