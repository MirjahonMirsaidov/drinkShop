from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from modeltranslation.admin import TranslationAdmin
from .models import *


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):

    list_display = ('id', 'name', 'view_products_link')
    search_fields = ('name',)
    list_display_links = ('name',)

    def view_products_link(self, obj):
        count = obj.product_set.count()
        url = (
                reverse("admin:product_product_changelist")
                + "?"
                + urlencode({"category__id": f"{obj.id}"})
        )
        return format_html('<b><a href="{}">{} Products</a></b>', url, count)

    view_products_link.short_description = "Products"


@admin.register(Brand)
class BrandAdmin(TranslationAdmin):

    list_display = ('id', 'name', 'view_products_link')
    search_fields = ('name',)
    list_display_links = ('name',)

    def view_products_link(self, obj):
        count = obj.product_set.count()
        url = (
                reverse("admin:product_product_changelist")
                + "?"
                + urlencode({"brand__id": f"{obj.id}"})
        )
        return format_html('<b><a href="{}">{} Products</a></b>', url, count)

    view_products_link.short_description = "Products"


class ProductImageAdmin(admin.TabularInline):
    model = Image


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductImageAdmin]
    list_display = ('id', 'title', 'category', 'brand', 'price', 'size', 'stock_count', 'created_at')
    list_display_links = ('title',)
    list_filter = ('created_at', 'category', 'brand')
    list_editable = ('price', 'stock_count')
    search_fields = ('title', 'brand__name', 'category__name')
    list_per_page = 10

    class Meta:
        model = Product
#
#
# @admin.register(Image)
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'product', 'image', 'image_tag', )
#     readonly_fields = ('image_tag',)
#     list_display_links = ('product',)