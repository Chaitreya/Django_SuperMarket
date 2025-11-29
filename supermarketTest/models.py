from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class Customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    stock_quantity = models.IntegerField()
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Sale(models.Model):
    customer_id = models.ForeignKey(
        Customer,
        on_delete = models.DO_NOTHING,
    )
    total_price = models.IntegerField()
    sale_date = models.DateTimeField()

class Sale_Items(models.Model):
    product_id = models.ForeignKey(
        Product,
        on_delete = models.DO_NOTHING,
    )
    sale_id = models.ForeignKey(
        Sale,
        on_delete = models.CASCADE,
    )
    quantity_sold = models.IntegerField()
    unit_price = models.IntegerField()
    

