from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage


def products(request):
    link_img = Product.objects.prefetch_related('productimage_set')
    products_with_images = link_img.values('id','name', 'price', 'productimage__image_path')

    # Pasa la lista a la plantilla
    context = {'products': products_with_images}
    
    return render(request, 'products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Aquí puedes hacer cualquier cosa con el objeto del producto
    context = {'product': product}

    return render(request, 'product_detail.html', context)