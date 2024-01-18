from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import JsonResponse
from products.models import Product
from django.shortcuts import render
from django.contrib import messages
from .models import CartItem
import json


# Create your views here.
def cart(request):
    user_id = request.user
    cart = Product.objects
    products = cart.values(
        'name', 'price', 'image_path', 'cart_items__quantity', 'id', 'name_detail'
        ).filter(cart_items__user_id=user_id)

    context = {'products': products}

    return render(request, 'cart/cart.html', context)


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
            # Si el elemento ya existe, simplemente actualiza la cantidad
            cart_item.quantity = quantity
            cart_item.save()

        return JsonResponse({'message': 'Product added to cart successfully'})
    else:
        return JsonResponse({'message': 'User not authenticated'}, status=401)
    

def delete_to_cart(request, product_id):
    if request.user.is_authenticated:
        user_id = request.user.idx
        user = get_object_or_404(User, id=user_id)
        product = get_object_or_404(Product, id=product_id)

        # Filtra y elimina el CartItem específico
        cart_item = CartItem.objects.filter(user=user, product=product).first()
        if cart_item:
            cart_item.delete()

        return JsonResponse({'message': 'Product deleted to cart successfully'})
    else:
        return JsonResponse({'message': 'User not authenticated'}, status=401)  