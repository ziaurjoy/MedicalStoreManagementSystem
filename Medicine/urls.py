from django.urls import path, include
from Medicine.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'list', MedicinneAPIViews, basename='medicine'),
router.register(r'details', MedicineDetailsAPIViews, basename='medicine-details'),

urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
]
