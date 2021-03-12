from django.urls import path, include

from Company.views import CompanyAPIViews, CompanyAccountAPIView



from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'details', CompanyAPIViews, basename='company-details'),
router.register(r'account', CompanyAccountAPIView, basename='company-account')
urlpatterns = router.urls



urlpatterns = [
    path('api/', include(router.urls)),
]
