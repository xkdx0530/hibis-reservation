from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.booking_create, name='booking_create'),
    path('list/', views.booking_list, name='booking_list'),
    path('cancel/<int:pk>/', views.booking_cancel, name='booking_cancel'),
]
