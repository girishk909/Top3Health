"""healthcare URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout
from django.urls import reverse


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('top3health/', include('django.contrib.auth.urls')),
    path('', include('top3health.urls')),
    
]

