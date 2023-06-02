from cgitb import lookup
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import CollectionViewSet, ProductViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('collections', CollectionViewSet)

procuct_routers = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
procuct_routers.register('reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + procuct_routers.urls
#     path("products/<int:pk>", ProductDetail.as_view(), name="ProductDetail"),
#     path("collections/", CollectionList.as_view(), name="CollectionList"),
#     path("collections/<int:pk>", CollectionDetail.as_view(), name="CollectionDetail"),
#     ]
