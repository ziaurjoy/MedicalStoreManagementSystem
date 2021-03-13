from django.urls import path, include
from Employee.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'list', EmployeeAPIView, basename='employee-list'),
router.register(r'salary', EmployeeSalaryAPIView, basename='employee-salary'),
router.register(r'bank', EmployeeBankAPIView, basename='employee-bank'),


urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
]