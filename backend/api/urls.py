from .views import *
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout
from django.urls import reverse
urlpatterns = [
    path('users/<int:user_id>',user.as_view()),
]