from django.urls import path
from . import views

urlpatterns = [
    path('jclapp/', views.indexpg, name='jclapp'),
]