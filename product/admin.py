from admin_interface.models import Theme
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(Theme)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'view_products_link')
    search_fields = ('name',)

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
class BrandAdmin(admin.ModelAdmin):

    list_display = ('name', 'view_products_link')
    search_fields = ('name',)

    def view_products_link(self, obj):
        count = obj.product_set.count()
        url = (
                reverse("admin:product_product_changelist")
                + "?"
                + urlencode({"brand__id": f"{obj.id}"})
        )
        return format_html('<b><a href="{}">{} Products</a></b>', url, count)

    view_products_link.short_description = "Products"


class ProductImageAdmin(admin.StackedInline):
    model = Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ('id', 'title', 'category', 'brand', 'price', 'size', 'stock_count')
    list_filter = ('created_at', 'price', 'category', 'brand')
    list_editable = ('price', 'stock_count')
    search_fields = ('title', 'brand__name', 'category__name')
    list_per_page = 5

    class Meta:
        model = Product


@admin.register(Image)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'image_tag', )
    readonly_fields = ('image_tag',)