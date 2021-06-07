from django.urls import path
from .views import *


urlpatterns = [
    path('detail/<slug:slug>', ProductDetailView.as_view()),
    path('list', ProductListView.as_view()),
    path('category/list', CategoryListView.as_view()),
    path('brand/list', BrandListView.as_view()),
]