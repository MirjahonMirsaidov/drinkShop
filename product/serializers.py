from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    image = ImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'category', 'brand', 'image', 'price', 'size', 'stock_count')