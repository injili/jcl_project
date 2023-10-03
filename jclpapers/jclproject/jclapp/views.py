from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order, OrderItem
from django.http import HttpResponse
from django.template import loader


def landing_page(request):
    products = Product.objects.all()
    return render(request, 'landing_page.html', {'products': products})

def marketplace(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'marketplace.html', {'product': product})


def checkout(request):
    if request.method == 'POST':
        # Process the order and save it to the database
        customer_name = request.POST['customer_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        shipping_address = request.POST['shipping_address']

        # Create an order
        order = Order.objects.create(
            customer_name=customer_name,
            phone_number=phone_number,
            email=email,
            shipping_address=shipping_address
        )

        # Process order items from the shopping cart
        cart = request.session.get('cart', {})  # Get the shopping cart from the session
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=product_id)
            order_item = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

        # Clear the shopping cart
        request.session['cart'] = {}

        # Redirect to a thank-you page or order confirmation page
        return redirect('order_confirmation')

    return render(request, 'checkout.html')


def order_confirmation(request):
    if request.method == 'POST':
        # Retrieve customer details from the form
        customer_name = request.POST['customer_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        shipping_address = request.POST['shipping_address']

        # Create a new order
        new_order = Order(
            customer_name=customer_name,
            phone_number=phone_number,
            email=email,
            shipping_address=shipping_address,
            order_status='Pending'  # Set the initial order status as 'Pending'
        )
        new_order.save()  # Save the order to the database

        # You can also add logic to save order items associated with this order
        # Retrieve cart items from the session and associate them with the new order
        cart_items = request.session.get('cart', {})  # Assuming you store cart items in the session
        for product_id, quantity in cart_items.items():
            # Add logic to create and save order items associated with this order
            # Example: OrderItem.objects.create(order=new_order, product=product, quantity=quantity)

            def landing_page(request):
                pass
            

            def marketplace(request, product_id):
                pass


        def checkout(request):
            if request.method == 'POST':
                # Process the order and save it to the database
                customer_name = request.POST['customer_name']
                phone_number = request.POST['phone_number']
                email = request.POST['email']
                shipping_address = request.POST['shipping_address']

                # Create an order
                order = Order.objects.create(
                    customer_name=customer_name,
                    phone_number=phone_number,
                    email=email,
                    shipping_address=shipping_address
                )

                # Process order items from the shopping cart
                cart = request.session.get('cart', {})  # Get the shopping cart from the session
                for product_id, quantity in cart.items():
                    product = get_object_or_404(Product, pk=product_id)
                    order_item = OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity
                    )

                # Clear the shopping cart
                request.session['cart'] = {}

                # Redirect to a thank-you page or display a confirmation message
                # For now, we'll redirect to the landing page
                return redirect('landing_page')

            return render(request, 'checkout.html')


        def order_confirmation(request):
            if request.method == 'POST':
                # Retrieve customer details from the form
                customer_name = request.POST['customer_name']
                phone_number = request.POST['phone_number']
                email = request.POST['email']
                shipping_address = request.POST['shipping_address']

                # Create a new order
                new_order = Order(
                    customer_name=customer_name,
                    phone_number=phone_number,
                    email=email,
                    shipping_address=shipping_address,
                    order_status='Pending'  # Set the initial order status as 'Pending'
                )
                new_order.save()  # Save the order to the database

                # You can also add logic to save order items associated with this order
                # Retrieve cart items from the session and associate them with the new order
                cart_items = request.session.get('cart', {})  # Assuming you store cart items in the session
                for product_id, quantity in cart_items.items():
                    # Add logic to create and save order items associated with this order
                    # Example: OrderItem.objects.create(order=new_order, product=product, quantity=quantity)

                # Clear the shopping cart from the session
                    request.session['cart'] = {}

                # Redirect to a thank-you page or display a confirmation message
                # For now, we'll redirect to the landing page
                    return redirect('landing_page')

            return render(request, 'order_confirmation.html')


        def order_history(request):
            # Get the user's order history (assuming you have a user ID)
            user_orders = Order.objects.filter(user=request.user)
            return render(request, 'order_history.html', {'user_orders': user_orders})
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=product_id)
            order_item = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

        # Clear the shopping cart
        request.session['cart'] = {}

        # Redirect to a thank-you page or display a confirmation message
        # For now, we'll redirect to the landing page
        return redirect('landing_page')
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=product_id)
            order_item = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

        # Clear the shopping cart
        request.session['cart'] = {}

        # Redirect to a thank-you page or display a confirmation message
        # For now, we'll redirect to the landing page
        return redirect('landing_page')

    return render(request, 'order_confirmation.html')


def order_history(request):
    # Get the user's order history (assuming you have a user ID)
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'user_orders': user_orders})
