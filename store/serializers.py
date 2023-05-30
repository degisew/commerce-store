from decimal import Decimal
from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')


    def calculate_tax(self, product:Product):
        return product.unit_price * Decimal(1.1)
