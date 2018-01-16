"""ComBoard URL Configuration
The `urlpatterns` list routes URLs (with regex handle) to views.
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views 
from comapi import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)', views.UserDetail.as_view()),
    url(r'^boards/$', views.BoardList.as_view()),
    url(r'^boards/(?P<pk>[0-9]+)', views.BoardDetail.as_view()),
    url(r'^board_posts/(?P<pk>[0-9]+)', views.BoardPostList.as_view()),
    url(r'^accounts/login/', auth_views.LoginView.as_view()),
]
