from django.contrib.auth.models import AbstractUser
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True)
    weight = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    grade = models.CharField(max_length=200, null=True)
    sheets_in_ream = models.IntegerField(null=True)
    thickness = models.CharField(max_length=200, null=True)
    quality = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    quantity = models.IntegerField(null=True)
    image = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.name

class CustomerProfile(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email_address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    whatsapp_number = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    street_address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.name

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.product.name
