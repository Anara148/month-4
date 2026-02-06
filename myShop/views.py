from django.shortcuts import render, get_object_or_404
from . import models

def all_categories(request):
    categories = models.Category.objects.all()
    return render(
            request,
            'categories.html',
            {
                    "categories": categories
            }
        )
    

def all_products(request):
    products = models.Product.objects.all()
    return render(
            request,
            'products.html',
            {
                    "products": products
            }
        )


def category_products(request, id):
    category = get_object_or_404(models.Category, id=id)
    products = category.products.all()
    return render(
            request,
            'category_products.html',
            {            
                    "products": products,
                    "category": category     
            }
        )