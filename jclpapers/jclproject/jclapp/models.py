from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    shipping_address = models.TextField()
    order_status = models.CharField(max_length=20, default='Pending')  # You can define order statuses like 'Pending', 'Delivered', etc.
    products = models.ManyToManyField(Product, through='OrderItem')

    def __str__(self):
        return f'Order #{self.pk}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


class Recommendation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recommended_products = models.ManyToManyField(Product, related_name='recommended_by')

    def __str__(self):
        return f'Recommendations for {self.product.name}'
