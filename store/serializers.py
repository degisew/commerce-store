from rest_framework import serializers


class ProductSerializers(serializers.Serializer):
    title = serializers.CharField()
    unit_price = serializers.DecimalField(max_digits=5, decimal_places=2)