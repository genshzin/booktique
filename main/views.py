import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)

    # Mengambil query pencarian dari parameter GET
    query = request.GET.get('query', '')
    if query:
        products = products.filter(name__icontains=query)  # Filter berdasarkan nama produk

    # Mengambil parameter sort dan order dari URL
    sort_by = request.GET.get('sort', '')
    order = request.GET.get('order', '')

    # Mengurutkan produk hanya jika kedua dropdown terpilih
    if sort_by and order:
        if sort_by == 'name':
            products = products.order_by('name' if order == 'asc' else '-name')
        elif sort_by == 'price':
            products = products.order_by('price' if order == 'asc' else '-price')
        elif sort_by == 'stock':
            products = products.order_by('stock_quantity' if order == 'asc' else '-stock_quantity')

    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'npm': '2306165553',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)



def about(request):
    return render(request, "about.html")

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def edit_product(request, id):
    product = Product.objects.get(pk = id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Invalid username or password.')  # Tambahkan pesan kesalahan di sini

    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
