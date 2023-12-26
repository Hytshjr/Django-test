from django.shortcuts import render
from .models import Product, ProductImage


def index(request):
    products_with_images = Product.objects.prefetch_related('productimage_set').all()

    # Construye una lista con la información deseada
    product_data = []
    for product in products_with_images:
        product_info = {
            'name': product.name,
            'price': product.price,
            'image_path': product.productimage_set.first().image_path if product.productimage_set.exists() else None,
        }
        product_data.append(product_info)

    # Pasa la lista a la plantilla
    context = {'products': product_data}
    
    return render(request, 'home.html', context)