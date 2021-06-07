from django.contrib import admin

from .models import *


admin.site.register(Category)
admin.site.register(Brand)


class ProductImageAdmin(admin.StackedInline):
    model = Image

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product

@admin.register(Image)
class ProductImageAdmin(admin.ModelAdmin):
    pass