import django_filters
from django.db.models import Max, Count, Value
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import *


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['price']
    search_fields = ['brand__name', 'category__name', 'title']
    filter_fields = ['brand', 'category']

    def get_queryset(self):
        try:
            min_price = self.request.GET.get('min')
            max_price = self.request.GET.get('max')
            if not min_price or min_price == '':
                min_price = 0
            if not max_price or max_price == '':
                max_price = Product.objects.aggregate(Max('price')).get('price__max')

            return Product.objects.filter(price__range=(min_price, max_price)).select_related('brand', 'category')
        except:
            return Product.objects.all()


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.annotate(product_count=Count('products')).values('id', 'name', 'product_count')


class CategoryWithProductsListView(ListAPIView):
    serializer_class = CategoryWithProductsSerializer
    queryset = Category.objects.all()


class BrandListView(ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
