from rest_framework import serializers

from .models import *


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('image',)


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class ProductInsideCategorySerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'brand', 'images', 'price', 'size', 'stock_count', 'description')


class CategoryWithProductsSerializer(serializers.ModelSerializer):
    products = ProductInsideCategorySerializer(required=False, many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'products')


class CategorySerializer(serializers.ModelSerializer):
    products = ProductInsideCategorySerializer(required=False, many=True)
    product_count = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'products', 'slug', 'product_count')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'category', 'brand', 'images', 'price', 'size', 'stock_count', 'description')