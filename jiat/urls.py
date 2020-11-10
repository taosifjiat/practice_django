from django.urls import path
from .views import *
urlpatterns = [
    path('friends',show_friends),
    
]