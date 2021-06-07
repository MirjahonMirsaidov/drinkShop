from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


class ProductImageAdmin(admin.StackedInline):
    model = Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ('id', 'title', 'category', 'brand', 'price', 'size', 'stock_count')
    list_filter = ('category', 'brand', 'price', 'size')

    class Meta:
        model = Product


@admin.register(Image)
class ProductImageAdmin(admin.ModelAdmin):
    pass