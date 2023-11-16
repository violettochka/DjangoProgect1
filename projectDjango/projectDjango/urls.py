"""
URL configuration for projectDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import main, about, profile, set_password, set_userdata, login, logout, register, deactivate
urlpatterns = [
    path('', main),
    path('about/', about),
    path('profile/<str:username>/', profile),
    path('article/<article>/', include('myapp.urls_article')),
    path('topics/', include('myapp.urls_topics') ),
    path('set-password/', set_password),
    path('set-userdata/', set_userdata),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('deactivate/', deactivate)
]
