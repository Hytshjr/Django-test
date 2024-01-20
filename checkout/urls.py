from django.urls import path
from . import views

urlpatterns = [
    path('delivery/', views.delivery, name='delivery'),
]