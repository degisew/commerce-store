from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request':self.request}
class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.count() > 0:
            return Response(
                {
                    "error": "The Object can't be deleted because it's associated with order items."
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.annotate(
            products_count=Count('products')).all()
    serializer_class = CollectionSerializer


class CollectionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
       
    def delete(self, request, pk):
       collection = get_object_or_404(Collection, pk=pk)
       if collection.products.count() > 0:
         return Response(
             {
                'error': 'Collection cannot be deleted because it includes one or more products.'
            },
             status=status.HTTP_405_METHOD_NOT_ALLOWED)
       collection.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)

