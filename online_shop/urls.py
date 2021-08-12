from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('product/', views.product, name='product'),
    path('updateOrder/<str:pk>:/', views.updateOrder, name='updateOrder'),
    path('delete/<str:pk>/', views.deleteOrder, name='deleteOrder'),
    path('createOrder/', views.createOrder, name='createOrder'),
    path('registrationPage/', views.registrationPage, name='registrationPage'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logoutPage/', views.logoutPage, name='logoutPage')
]