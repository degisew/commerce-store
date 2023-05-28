from django.contrib import admin
from .models import Collection, Product

# Customizing admin list page 
@admin.register(Product) # shorter way of registering models
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']


admin.site.register(Collection)
# admin.site.register(Product)