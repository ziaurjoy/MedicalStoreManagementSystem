from django.urls import path, include

from Company.views import CompanyAPIViews

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', CompanyAPIViews, basename='company')
urlpatterns = router.urls



urlpatterns = [
    path('api/', include(router.urls)),
]
