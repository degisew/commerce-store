from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers
from store import serializers


@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializers(product)
    return Response(serializer.data)
