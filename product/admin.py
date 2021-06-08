from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'view_products_link')

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
    pass


class ProductImageAdmin(admin.StackedInline):
    model = Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ('id', 'title', 'category', 'brand', 'price', 'size', 'stock_count')
    list_filter = ('category', 'brand', 'price')
    search_fields = ('title', 'brand__name', 'category__name')

    class Meta:
        model = Product


@admin.register(Image)
class ProductImageAdmin(admin.ModelAdmin):
    pass