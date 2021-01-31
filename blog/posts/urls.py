from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.userBlogs, name="blogs"),
    path('favourites/', views.userFav, name='favourites'),
    path('first/', views.UserFirst, name='profile'),
    path('profile/', views.UserNormal, name='profile')
]