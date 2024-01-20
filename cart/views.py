from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import JsonResponse
from products.models import Product
from django.contrib import messages
from .models import CartItem
import json


# Create your views here.
def cart(request):
    user_id = request.user.id

    if user_id:
        cart = Product.objects
        products = cart.values(
            'name', 'price', 'image_path', 
            'cart_items__quantity', 'id', 'name_detail'
            ).filter(cart_items__user_id=user_id)
        
        total = 0
        
        for product in products:
            suma = product['price']*product['cart_items__quantity']
            total += suma

        total_price = [total]

        context = {'products': products, 'price':total_price}

        return render(request, 'cart/cart.html', context)
    else:
        messages.error(request, 'You need to loged.')
        return redirect('login')


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        payload = json.loads(request.body)
        quantity = payload.get('quantity', 1)

        # Crear o actualizar el item del carrito
        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            user=request.user,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity = quantity
            cart_item.save()

        return JsonResponse({
            'message': 'Product added to cart successfully'
            })
    else:
        return JsonResponse({
            'message': 'User not authenticated'
            }, status=401)
    

def delete_to_cart(request, product_id):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = get_object_or_404(User, id=user_id)
        product = get_object_or_404(Product, id=product_id)
        cart_item = CartItem.objects
        cart_item = cart_item.filter(user=user, product=product)
        
        # Filtra y elimina el CartItem específico
        if cart_item.first():
            cart_item.first().delete()

        return JsonResponse({
            'message': 'Product deleted to cart successfully'
            })
    else:
        return JsonResponse({
            'message': 'User not authenticated'
            }, status=401)  