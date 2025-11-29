from django.urls import path
from . import views

app_name = "supermarketTest"
urlpatterns = [
    # Product Urls
    path('all_products',views.all_products, name="all_products"),
    path('detail_product/<int:product_id>', views.detail_product, name="detail_product"),
    path('add_product', views.add_product, name="add_product"),
    path('edit_product/<int:product_id>', views.edit_product , name="edit_product"),
    path('delete_product/<int:product_id>', views.delete_product , name="delete_product"),

    # Category Urls
    path('all_categories', views.all_categories, name="all_categories")
]