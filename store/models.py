from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    GOLD_MEMBERSHIP = 'G',
    SILVER_MEMBERSHIP = 'S',
    BRONZE_MEMBERSHIP = 'B',

    MEMBERSHIP_CHOICES =[
        (BRONZE_MEMBERSHIP, 'Bronze'),
        (GOLD_MEMBERSHIP, 'Gold'),
        (SILVER_MEMBERSHIP, 'Silver'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=BRONZE_MEMBERSHIP)

    last_update = models.DateTimeField(auto_now=True)


class Order(models.Model):
    PENDING_STATUS = 'P',
    COMPLETED_STATUS = 'C',
    FAILED_STATUS = 'F',

    PAYMENT_STATUS_CHOICES = [
        (PENDING_STATUS, 'Pending'),
        (COMPLETED_STATUS, 'Completed'),
        (FAILED_STATUS, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PENDING_STATUS)