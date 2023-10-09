from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Product, Order, OrderItem, Cart

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def products(request):
    products = Product.objects.all()
    template = loader.get_template('products.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context))

def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())

def confirm(request):
    products = Product.objects.all()
    template = loader.get_template('confirm.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render())

def ordersuccessful(request):
    template = loader.get_template('ordersuccessful.html')
    return HttpResponse(template.render())

def display_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    other_products = Product.objects.exclude(pk=product_id)[:2]  # Get two other products

    print("Selected Product:", product.name)
    for other_product in other_products:
        print("Other Product:", other_product.name)

    context = {
        'selected_product': product,
        'other_products': other_products,
    }
    return render(request, 'products.html', context)