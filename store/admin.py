from django.contrib import admin
from .models import Collection, Product, Customer

# Customizing admin list page 
@admin.register(Product) # shorter way of registering models
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10
    ordering = ['title', 'unit_price']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']


admin.site.register(Collection)
