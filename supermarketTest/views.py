from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse
from supermarketTest.models import Product, Category
from django.utils import timezone


# Create your views here.

#  Product views
def all_products(request):
    products = Product.objects.all().order_by('name')
    return render(request, "supermarket/products.html", {"product_list":products})

def detail_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "supermarket/detail_product.html", {"product": product})

def add_product(request):
    if request.method == "POST":
        product = Product(
            name=request.POST['name'],
            price=request.POST['price'],
            description=request.POST['description'],
            stock_quantity=request.POST['stock_quantity'],
            category_id_id=request.POST['category_id'],
        )
        product.created_at = timezone.now()
        product.updated_at = timezone.now()
        product.save()

    else:
        categories = Category.objects.all()
        return render(request, "supermarket/add_product.html", {"categories": categories})
    
    return redirect('supermarketTest:all_products')

def edit_product(request,product_id):
    product = get_object_or_404(Product,pk=product_id)

    if request.method == "POST":
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.stock_quantity = request.POST['stock_quantity']
        product.category_id_id = request.POST['category_id']
        product.updated_at = timezone.now()

        product.updated_at = timezone.now()
        product.save()

    else:    
        categories = Category.objects.all()
        return render(request, "supermarket/edit_product.html", {"categories": categories , 'product':product})
    
    return redirect('supermarketTest:all_products')

def delete_product(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    product.delete()
    return redirect('supermarketTest:all_products')


#   Category views

def all_categories(request):
    categories = Category.objects.all().order_by("category_name")
    return render(request, "supermarket/categories.html", {"categories": categories})

def detail_category(request,category_id):
    category = get_object_or_404(Category,pk=category_id)
    return render(request, "supermarket/detail_category.html", {"category":category})

def add_category(request):
    if request.method == "POST":
        category = Category(
            category_name = request.POST['name'],
            description = request.POST['description']
        )
        category.save()

    else:
        return render(request, "supermarket/add_category.html")
    
    return redirect('supermarketTest:all_categories')

def delete_category(request, category_id):
    category = get_object_or_404(Category,pk=category_id)
    category.delete()
    return redirect('supermarketTest:all_categories')

def edit_category(request, category_id):
    if request.method == "POST":
        category = get_object_or_404(Category, pk = category_id)
        category.category_name = request.POST['name']
        category.description = request.POST['description']
        category.save()

    else:
        category = get_object_or_404(Category,pk = category_id)
        return render(request, 'supermarket/edit_category.html', {"category": category})
    
    return redirect('supermarketTest:all_categories')