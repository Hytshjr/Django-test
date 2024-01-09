from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage


def products(request):
    link_img = Product.objects.prefetch_related('productimage_set')
    products_with_images = link_img.values(
        'id','name', 'name_detail', 'price', 'categories', 'productimage__image_path'
        )

    # Pasa la lista a la plantilla
    context = {'products': products_with_images}
    
    return render(request, 'products.html', context)


def product_categories(request, product_categories):
    query_img = Product.objects
    query_img.prefetch_related('productimage_set'),

    products_with_images = query_img.values(
        'name', 'name_detail', 'price', 'productimage__image_path'
        ).filter(categories=product_categories)


    # Pasa la lista a la plantilla
    context = {'products': products_with_images}
    
    return render(request, 'products.html', context)


def product_detail(request, name_detail):
    query_product = Product.objects
    query_product.prefetch_related('productimage_set'),

    product = query_product.values(
        'name', 'name_detail', 'description', 'price', 'productimage__image_path', 'delivery', 'collect'
    ).filter(name_detail=name_detail)

    # Aquí puedes hacer cualquier cosa con el objeto del producto
    context = {'products': product}

    return render(request, 'product_detail.html', context)