import datetime
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    query = request.GET.get('query')
    if query:
        results = Product.objects.filter(name__icontains=query)  # Adjust the filter as needed

    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'npm': '2306165553',
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
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
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
            response = HttpResponseRedirect(reverse('main:about'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Invalid username or password. Please try again.')  # Tambahkan pesan kesalahan di sini

    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get('name'))
    author = strip_tags(request.POST.get('author'))
    description = strip_tags(request.POST.get('description'))
    stock_quantity = request.POST.get('stock_quantity')
    price = request.POST.get('price')
    user = request.user

    new_product = Product(name=name, author=author, description=description, stock_quantity=stock_quantity, price=price, user=user)
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_mood = Product.objects.create(
            user=request.user,
            name=data['name'],
            author=data['author'],
            description=data['description'],
            stock_quantity=data['stock_quantity'],
            price=data['price'],
        )

        new_mood.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def delete_product_flutter(request, id):
    if request.method == 'GET':  # Changed from checking POST
        try:
            product = Product.objects.get(pk=id)
            product.delete()
            return JsonResponse({"status": "success"}, status=200)
        except Product.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Product not found"}, 
                status=404
            )
        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": str(e)}, 
                status=500
            )
    
    return JsonResponse(
        {"status": "error", "message": "Invalid method"}, 
        status=405
    )

@csrf_exempt
def edit_product_flutter(request, id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(pk=id)
            data = json.loads(request.body)
            
            # Update fields
            product.name = data['name']
            product.author = data['author']
            product.description = data['description']
            product.stock_quantity = int(data['stock_quantity'])
            product.price = int(data['price'])
            
            product.save()
            return JsonResponse({"status": "success"}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Product not found"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)

   
