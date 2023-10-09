from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('products/', views.products, name='products'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirm/', views.confirm, name='confirm'),
    path('ordersuccessful/', views.ordersuccessful, name='ordersuccessful'),
    path('products/<int:product_id>/', views.display_product, name='display_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)