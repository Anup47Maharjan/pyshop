from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages


def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    total_order = order.count()
    pending_order = order.filter(status='pending').count()
    in_process = order.filter(status='in process').count()
    content = {'customers': customer, 'orders': order, 'total_order': total_order, 'pending_order': pending_order,
               'in_process': in_process}
    return render(request, 'home.html', content)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    total_order = order.count()
    myfilter = OrderFilter(request.GET, queryset=order)
    order = myfilter.qs
    content = {'orders': order, 'customers': customer, 'total_order': total_order, 'myfilter': myfilter}
    return render(request, 'customer.html', content)


def product(request):
    product = Product.objects.all()
    content = {'products': product}
    return render(request, 'product.html', content)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    forms = OrderForm(instance=order)
    if request.method == 'POST':
        forms = OrderForm(request.POST, instance=order)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    content = {'orders': order, 'forms': forms}
    return render(request, 'updateOrder.html', content)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('home')
    content = {'orders': order}
    return render(request, 'deleteOrder.html', content)


def createOrder(request):
    forms = OrderForm()
    if request.method == "POST":
        forms = OrderForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    content = {'forms': forms}
    return render(request, 'createOrder.html', content)


def registrationPage(request):
    forms = CreateUserForm()
    if request.method == "POST":
        forms = CreateUserForm(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + username)
            return redirect('loginPage')
    content = {'forms': forms}
    return render(request, 'registrationPage.html', content)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
    content = {}
    return render(request, 'loginPage.html', content)


def logoutPage(request):
    logout(request)
    return redirect('loginPage')