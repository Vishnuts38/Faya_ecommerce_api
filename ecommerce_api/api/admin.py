from django.contrib import admin

from .models import CustomUser,Product


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'customer', 'product_name', 'description', 'price', 'registration_date', 'is_active')
#     list_filter = ('customer', 'registration_date', 'is_active') 
#     date_hierarchy = 'registration_date'
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Product)