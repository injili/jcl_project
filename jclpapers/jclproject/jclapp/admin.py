from django.contrib import admin
from .models import Product, CustomerProfile, Order, OrderItem, Cart

admin.site.site_header = 'JCL Papers Admin'
admin.site.site_title = 'JCL Papers Admin'
admin.site.index_title = 'JCL Papers Admin'

admin.site.register(Product)
admin.site.register(CustomerProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)