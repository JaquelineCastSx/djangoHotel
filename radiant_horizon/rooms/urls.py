from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('clients/clientDetail/<int:id>', views.details, name='details'),
    path('reservations/', views.reservations, name='reservations'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/roomDetail/<int:id>', views.room_detail, name='room_detail'),
    path('roomt/', views.roomt, name='roomt'),
    path('workers/', views.workers, name='workers'),
    path('workers/workerDetail/<int:id>', views.worker_detail, name='worker_detail'),
    path('payments/', views.paymenttype, name='payments'),
]