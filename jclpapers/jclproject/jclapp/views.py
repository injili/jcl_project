from django.http import HttpResponse
from django.template import loader
# from django.db.models import Product, CustomUser, Order, OrderItem, Cart

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def products(request):
    template = loader.get_template('products.html')
    return HttpResponse(template.render())

def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())

def confirm(request):
    template = loader.get_template('confirm.html')
    return HttpResponse(template.render())

def ordersuccessful(request):
    template = loader.get_template('ordersuccessful.html')
    return HttpResponse(template.render())