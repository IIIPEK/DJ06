from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('products/', views.products, name='product'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
]