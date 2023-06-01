from django.urls import path
from .views import CollectionList, ProductDetail, ProductList, CollectionDetail


urlpatterns = [
    path("products/", ProductList.as_view(), name="ProductList"),
    path("products/<int:pk>", ProductDetail.as_view(), name="ProductDetail"),
    path("collections/", CollectionList.as_view(), name="CollectionList"),
    path("collections/<int:pk>", CollectionDetail.as_view(), name="CollectionDetail"),
    ]
