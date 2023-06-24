from uuid import uuid4
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=200)
    featured_product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, related_name="collections"
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["title"]


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self) -> str:
        return self.description

    class Meta:
        ordering = ["description"]


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(1)]
    )
    inventory = models.IntegerField(validators=[MinValueValidator(1)])
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, related_name='products')
    promotions = models.ManyToManyField(Promotion, blank=True, null=True)

    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["title"]


class Customer(models.Model):
    GOLD_MEMBERSHIP = "G"
    SILVER_MEMBERSHIP = "S"
    BRONZE_MEMBERSHIP = "B"

    MEMBERSHIP_CHOICES = [
        (BRONZE_MEMBERSHIP, "Bronze"),
        (GOLD_MEMBERSHIP, "Gold"),
        (SILVER_MEMBERSHIP, "Silver"),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=BRONZE_MEMBERSHIP
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["first_name"]


class Order(models.Model):
    PENDING_STATUS = "P"
    COMPLETED_STATUS = "C"
    FAILED_STATUS = "F"

    PAYMENT_STATUS_CHOICES = [
        (PENDING_STATUS, "Pending"),
        (COMPLETED_STATUS, "Completed"),
        (FAILED_STATUS, "Failed"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PENDING_STATUS
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip = models.CharField(max_length=200, null=True)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True
    )

    def __str__(self) -> str:
        return self.city

    class Meta:
        ordering = ["city"]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    # use uuid to make more secure
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    #unique constraint to avoid having duplicate instances.
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'product'],
                name='unique_cart_product'
            )
        ]

class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
