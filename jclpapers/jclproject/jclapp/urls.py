from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('products/', views.products, name='products'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirm/', views.confirm, name='confirm'),
    path('ordersuccessful/', views.ordersuccessful, name='ordersuccessful'),
]