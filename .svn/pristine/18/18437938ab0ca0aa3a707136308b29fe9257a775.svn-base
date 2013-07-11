# encoding: utf-8

from django.contrib import admin
import gocdn.settings as settings
from django.contrib import admin
from gocdn.product.models import *
from gocdn.product.forms import ProductAdminForm
class ProductAdmin(admin.ModelAdmin):
    #form = ProductAdminForm
    # sets values for how the admin site lists your products
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']


    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']

    # sets up slug to be generated from product name
    prepopulated_fields = {'slug' : ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    prepopulated_fields = {'slug' : ('name',)}

class CountryAdmin(admin.ModelAdmin):
    list_display = ['country',]
    list_display_links = ['country',]
    list_per_page = 20
    ordering = ['country_order']
    search_fields = ['country']

class PricingAdmin(admin.ModelAdmin):
    list_display = ['pricing_country','price_per_gb','price_per_tb',]
    list_display_links = ['pricing_country',]
    list_per_page = 20
    search_fields = ['pricing_country']



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(Pricing,PricingAdmin)