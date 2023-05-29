from django.urls import path
from .views import product_list, product_detail


urlpatterns = [
    path("products/", product_list, name="product_list"),
    path("products/<int:id>", product_detail, name="product_detail"),
    ]
