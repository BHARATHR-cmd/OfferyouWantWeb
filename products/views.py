from django.shortcuts import render

from .models import Product

# Create your views here.


def retrieve(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def contact(request):
    return render(request, 'contact.html')
