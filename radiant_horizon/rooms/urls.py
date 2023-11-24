from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.places, name='rooms'),
]