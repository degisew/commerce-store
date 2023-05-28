from django.contrib import admin
from .models import Collection, Product, Customer, Order

# Customizing admin list page 
@admin.register(Product) # shorter way of registering models
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status']
    list_editable = ['unit_price']
    list_per_page = 10
    ordering = ['title', 'unit_price']

    @admin.display(ordering='inventory') # Ordering logic for inventory_status
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'LOW'
        return 'OK'

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    ordering = []
admin.site.register(Collection)
