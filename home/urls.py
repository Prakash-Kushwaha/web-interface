from django.urls import path
from . import views

urlpatterns = [
    path('index', views.home),
    path('login', views.login),
    path('signup', views.signup),
    path('display', views.display),
]