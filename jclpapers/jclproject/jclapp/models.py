from django.contrib.auth.models import AbstractUser
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    sheets_in_ream = models.IntegerField()
    thickness = models.CharField(max_length=200)
    quality = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class CustomerProfile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    whatsapp_number = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name
