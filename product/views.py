import django_filters
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
        min = self.request.GET.get('min')
        max = self.request.GET.get('max')
        if not min or min == '':
            min = 0
        if not max or max == '':
            max = Product.objects.all().order_by('-price').first().price

        return Product.objects.filter(price__range=(min, max)).select_related('brand', 'category').order_by('-id')


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.all()


class BrandListView(ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()