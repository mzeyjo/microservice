from django.urls import path

from .views import ShopViewSet, OrderViewSet

urlspatterns = [
    path('shop', ShopViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    path('shop', ShopViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
    })),
]