from django.forms import ModelForm
from .models import *
import django_filters
from django_filters import DateFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ['customer', 'date_created']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def unauthenticated_user(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return func(request, *args, **kwargs)
    return wrapper


def allowed_user(allowed_roles=[]):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return func(request, *args, **kwargs)
                else:
                    return HttpResponse('you are not authorise here.')
        return wrapper
    return decorator


def admin_only(func):
    def wrapper(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            if group == 'gp_customer':
                return redirect('userPage')
            if group == 'admin':
                return func(request, *args, **kwargs)
            else:
                return HttpResponse('Group is not specified')
    return wrapper


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ['user']