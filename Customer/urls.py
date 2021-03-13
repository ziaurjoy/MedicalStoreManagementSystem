from django.urls import path, include
from Customer.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'list', CustomerAPIView, basename='medicine-details'),
router.register(r'request', CustomerRequestAPIView, basename='customer-request'),
router.register(r'bill', BillAPIView, basename='customer-bill'),
router.register(r'billdetails', BillDetailsAPIView, basename='customer-bill'),

urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
]
