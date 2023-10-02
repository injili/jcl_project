from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Product, Order, OrderItem
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')  # Redirect to product listing page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')  # Redirect to product listing page after login
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required
def place_order(request):
    user = request.user
    cart_items = ShoppingCart.objects.filter(user=user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    if request.method == 'POST':
        # Create a new order
        order = Order.objects.create(user=user, total_price=total_price)
        
        # Create order items based on items in the shopping cart
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
        
        # Clear the user's shopping cart
        cart_items.delete()
        
        return redirect('order_confirmation', order_id=order.id)
    
    return render(request, 'place_order.html', {'cart_items': cart_items, 'total_price': total_price})


# views.py
from django.shortcuts import render, redirect
from .models import Product, ShoppingCart
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(pk=product_id)
    
    # Check if the product is already in the user's cart
    existing_cart_item = ShoppingCart.objects.filter(user=user, product=product).first()
    
    if existing_cart_item:
        # If the product is already in the cart, increase the quantity
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        # If the product is not in the cart, create a new cart item
        ShoppingCart.objects.create(user=user, product=product, quantity=1)
    
    return redirect('view_cart')


# views.py
from django.shortcuts import render
from .models import ShoppingCart
from django.contrib.auth.decorators import login_required

@login_required
def view_cart(request):
    user = request.user
    cart_items = ShoppingCart.objects.filter(user=user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})


# views.py
from django.shortcuts import render, redirect
from .models import ShoppingCart
from django.contrib.auth.decorators import login_required

@login_required
def remove_from_cart(request, cart_item_id):
    user = request.user
    cart_item = ShoppingCart.objects.get(pk=cart_item_id)
    
    if cart_item.user == user:
        cart_item.delete()
    
    return redirect('view_cart')


# views.py
from django.shortcuts import render, redirect
from .models import ShoppingCart, Order, OrderItem
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    user = request.user
    cart_items = ShoppingCart.objects.filter(user=user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    if request.method == 'POST':
        # Create a new order
        order = Order.objects.create(user=user, total_price=total_price)
        
        # Create order items based on items in the shopping cart
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
        
        # Clear the user's shopping cart
        cart_items.delete()
        
        return redirect('order_confirmation', order_id=order.id)
    
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})



