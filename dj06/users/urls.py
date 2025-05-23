from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.redirect_to_login, name='root-redirect'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]