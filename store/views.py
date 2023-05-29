import imp
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers


@api_view()
def product_list(request):
    return Response("Ok")


@api_view()
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializers(product)
    return Response(serializer.data)
