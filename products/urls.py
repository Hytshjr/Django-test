from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<str:product_categories>/', views.product_categories, name='product_categories'),
    path('d/<str:name_detail>/', views.product_detail, name='product_detail'),
]