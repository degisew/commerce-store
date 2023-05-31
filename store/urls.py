from django.urls import path
from .views import product_list, product_detail, collection_list, collection_detail


urlpatterns = [
    path("products/", product_list, name="product_list"),
    path("products/<int:id>", product_detail, name="product_detail"),
    path("collections/", collection_list, name="collection_list"),
    path("collections/<int:id>", collection_detail, name="collection_detail"),
    ]
