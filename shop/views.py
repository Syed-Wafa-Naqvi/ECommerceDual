from django.shortcuts import render
from ..shop.forms import *
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.


def category_list(request):
  if request.method == 'GET':
      categories = Category.objects.all()
      return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, category_id):
  if request.method == 'GET':
      category = Category.objects.get(id=category_id)
      products = Product.objects.filter(category=category)
      return render(request, 'category_detail.html', {'category': category, 'products': products})

def add_category(request):
  if request.method == 'POST':
      form = CategoryForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return redirect('category_list')
  else:
      form = CategoryForm()
  return render(request, 'add_category.html', {'form': form})

def edit_category(request, category_id):
  category = Category.objects.get(id=category_id)
  if request.method == 'POST':
      form = CategoryForm(request.POST, request.FILES, instance=category)
      if form.is_valid():
          form.save()
          return redirect('category_list')
  else:
      form = CategoryForm(instance=category)
  return render(request, 'edit_category.html', {'form': form})

def delete_category(request, category_id):
  category = Category.objects.get(id=category_id)
  if request.method == 'POST':
      category.delete()
      return redirect('category_list')
  return render(request, 'delete_category.html', {'category': category})


def add_product(request):
  if request.method == 'POST':
      form = ProductForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return redirect('product_list')
  else:
      form = ProductForm()
  return render(request, 'add_product.html', {'form': form})

def edit_product(request, product_id):
  product = Product.objects.get(id=product_id)
  if request.method == 'POST':
      form = ProductForm(request.POST, request.FILES, instance=product)
      if form.is_valid():
          form.save()
          return redirect('product_list')
  else:
      form = ProductForm(instance=product)
  return render(request, 'edit_product.html', {'form': form})

def delete_product(request, product_id):
  product = Product.objects.get(id=product_id)
  if request.method == 'POST':
      product.delete()
      return redirect('product_list')
  return render(request, 'delete_product.html', {'product': product})

def product_list(request):
  products = Product.objects.all()
  return render(request, 'product_list.html', {'products': products})

def category_detail(request, category_id):
  category = Category.objects.get(id=category_id)
  products = Product.objects.filter(category=category)
  return render(request, 'category_detail.html', {'category': category, 'products': products})
