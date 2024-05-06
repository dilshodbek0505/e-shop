from django.shortcuts import render
from django.views import View

from .models import Product



def home(request):
    products = Product.objects.all()
    return render(request, 'index.html',{"products": products})


def product(request, pk):
    product = Product.objects.get(id = pk)

    return render(request, 'product.html', {"product": product})