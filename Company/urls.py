from django.urls import path, include

from Company.views import *



from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'details', CompanyAPIViews, basename='company-details'),
router.register(r'account', CompanyAccountAPIView, basename='company-account'),
router.register(r'bank', CompanyBankAPIView, basename='company-bank'),
urlpatterns = router.urls



urlpatterns = [
    path('api/', include(router.urls)),
    path('api/companybyname/<str:name>', CompanyNameViewSet.as_view(), name="companybyname"),
]
