from decimal import Decimal
from rest_framework import serializers
from .models import Cart, CartItem, Collection, Product, Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'slug', 'inventory',
                  'description', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'description', 'name']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)

''' another product serializer b/c not want to return
    all details of product inside cart items serializer '''
class MiniProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']

class CartItemSerializer(serializers.ModelSerializer):
    product = MiniProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item: CartItem):
        return cart_item.product.unit_price * cart_item.quantity
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']
    


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(read_only=True, many=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart: Cart):
       return sum([item.quantity * item.product.unit_price for item in cart.items.all()])
    
    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price'] 


class AddCartItemSerializer(serializers.ModelSerializer):
      product_id = serializers.IntegerField()

      # validate individual objects(this case product_id)
      def validate_product_id(self, value):
          if not Product.objects.filter(pk=value).exists():
              raise serializers.ValidationError('No Product with the given id was found.')
          return value
      ''' We don't want to store multiple instance of a single object.
          instead we should increase quantity of it '''
      def save(self, **kwargs):
         cart_id = self.context['cart_id'] # passed from the views
         product_id = self.validated_data['product_id']
         quantity = self.validated_data['quantity']

         try:
             cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
             cart_item.quantity += quantity
             cart_item.save()
             self.instance = cart_item
         except CartItem.DoesNotExist:
             self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
         return self.instance
          
      class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
    
