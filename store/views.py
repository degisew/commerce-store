from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import OrderItem, Product
from .serializers import ProductSerializers


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        serializer = ProductSerializers(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializers(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if product.orderitems.count() > 0:
            return Response({"error": "The Object can't be deleted because it's associated with order items."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
