from cgitb import lookup
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import CartItemViewSet, CartViewSet, CollectionViewSet, ProductViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('collections', CollectionViewSet)
router.register('carts', CartViewSet)

procuct_routers = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
procuct_routers.register('reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + procuct_routers.urls
