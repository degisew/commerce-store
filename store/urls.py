from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CollectionViewSet, ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('collections', CollectionViewSet)

urlpatterns = router.urls
# [
#     path("products/", ProductList.as_view(), name="ProductList"),
#     path("products/<int:pk>", ProductDetail.as_view(), name="ProductDetail"),
#     path("collections/", CollectionList.as_view(), name="CollectionList"),
#     path("collections/<int:pk>", CollectionDetail.as_view(), name="CollectionDetail"),
#     ]
