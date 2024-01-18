from django.shortcuts import render

from .models import Product


def products(request):

    products = Product.objects.values(
        'name', 'name_detail', 'price', 'image_path' 
        )


    # Pasa la lista a la plantilla
    context = {'products': products}
    
    return render(request, 'products.html', context)


def product_categories(request, product_categories):
    product_query = Product.objects
    product_query.select_related('categories')

    products = product_query.values(
        'name', 'name_detail', 'price', 'image_path', 'categories__category'
        ).filter(categories__category=product_categories)


    # Pasa la lista a la plantilla
    context = {'products': products}
    
    return render(request, 'products.html', context)


def product_detail(request, name_detail):
    product = Product.objects.values(
        'id', 'name', 'name_detail', 'price', 'image_path', 'description', 'delivery', 'collect', 'cart_items__quantity'
    ).filter(name_detail=name_detail)

    # Aquí puedes hacer cualquier cosa con el objeto del producto
    context = {'products': product}

    return render(request, 'product_detail.html', context)