from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder


def index(request):
  template = loader.get_template('store/index.html')
  return HttpResponse(template.render())

def products(request):
  template = loader.get_template('store/products.html')
  return HttpResponse(template.render())

def shop80(request):
  template = loader.get_template('store/shop80.html')
  return HttpResponse(template.render())

def shop70(request):
  template = loader.get_template('store/shop70.html')
  return HttpResponse(template.render())

def shop65(request):
  template = loader.get_template('store/shop65.html')
  return HttpResponse(template.render())

def store(request):
    # Assuming you want to keep the cart data retrieval logic
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    # Filter products by weight
    products_80gsm = Product.objects.filter(shop='shop80')
    products_70gsm = Product.objects.filter(shop='shop70')
    products_65gsm = Product.objects.filter(shop='shop65')

    context = {
        'products_80gsm': products_80gsm,  # Pass the filtered products to the template
        'products_70gsm': products_70gsm,
        'products_65gsm': products_65gsm,
        'cartItems': cartItems,
    }
    return render(request, 'store/store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		street=data['shipping']['street'],
		phone_number=data['shipping']['phone_number'],
		)

	return JsonResponse('Payment submitted..', safe=False)