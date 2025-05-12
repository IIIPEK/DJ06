from django.shortcuts import render
from django.http import HttpResponse

def products(request):
    return HttpResponse('products')

def product(request):
    return HttpResponse('product')

def order(request):
    return HttpResponse('order')

def orders(request):
    return HttpResponse('orders')
