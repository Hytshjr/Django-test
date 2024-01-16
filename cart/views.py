from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from .models import CartItem
from products.models import Product


# Create your views here.
def cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        quantity = int(request.POST.get('quantity', 1))

        # Crear o actualizar el item del carrito
        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            user=request.user,
            defaults={'quantity': quantity}
        )

        if not created:
            # Si el elemento ya existe, simplemente actualiza la cantidad
            cart_item.quantity += quantity
            cart_item.save()

        return JsonResponse({'message': 'Product added to cart successfully'})
    else:
        return JsonResponse({'message': 'User not authenticated'}, status=401)