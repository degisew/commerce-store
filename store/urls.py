from django.urls import path
from .views import CollectionList, ProductDetail, ProductList, collection_detail


urlpatterns = [
    path("products/", ProductList.as_view(), name="ProductList"),
    path("products/<int:id>", ProductDetail.as_view(), name="ProductDetail"),
    path("collections/", CollectionList.as_view(), name="CollectionList"),
    path("collections/<int:id>", collection_detail, name="collection_detail"),
    ]
