from django.http import HttpResponse
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect('users:login')

def login(request):
    return HttpResponse('login')

def register(request):
    return HttpResponse('register')

def logout(request):
    return HttpResponse('logout')



