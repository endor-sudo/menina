"""Defines URL patterns for users"""
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
  path('login/', LoginView.as_view(template_name='user/login.html'), name="login"),
  path('logout/', views.logout_view, name='logout')
]