from django.urls import path
from .views import User

urlpatterns = [
    path('users/<int:user_id>/', User.as_view(), name='user-detail'),
]
