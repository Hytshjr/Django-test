from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete_to_cart/<int:product_id>/', views.delete_to_cart, name='delete_to_cart'),

]



