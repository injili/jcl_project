from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
	path('store/', views.store, name="store"),
	path('products/', views.products, name="products"),
	path('shop80/', views.shop80, name="shop80"),
	path('shop70/', views.shop70, name="shop70"),
	path('shop65/', views.shop65, name="shop65"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]