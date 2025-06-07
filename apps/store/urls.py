from rest_framework_nested import routers
from apps.store.views import (
     CartItemViewSet,
     CartViewSet,
     CollectionViewSet,
     CustomerViewSet,
     OrderViewSet,
     ProductViewSet,
     ReviewViewSet
)

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('collections', CollectionViewSet, basename='collections')
router.register('customers', CustomerViewSet, basename='customers')
router.register('carts', CartViewSet, basename='carts')
router.register('orders', OrderViewSet, basename='orders')

procuct_routers = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
procuct_routers.register('reviews', ReviewViewSet, basename='product-reviews')
cart_routers = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_routers.register('items', CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + procuct_routers.urls + cart_routers.urls
