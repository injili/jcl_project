from django.contrib import admin
from .models import Product, Recommendation, Order, OrderItem


admin.site.register(Product)
admin.site.register(Recommendation)
admin.site.register(Order)
admin.site.register(OrderItem)
