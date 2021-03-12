#
#
# from Company.views import CompanyViewSet
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'create', CompanyViewSet, basename='company')
# urlpatterns = router.urls
#
#
# from django.urls import path, include
#
# urlpatterns = [
#     path('api/', include(router.urls)),
#
# ]

# from django.urls import path
# from Company import views
#
# urlpatterns = [
#     # path('api/persion/create', views.PersionCreate.as_view()),
#     # path('api/persion/list', views.PersionList.as_view()),
#     path('api/<int:id>', views.CompanyViewSet.as_view()),
#
# ]


from django.urls import path
from Company import views

urlpatterns = [
    path('api/create', views.CompanyCreate.as_view()),
    path('api/list', views.CompanyList.as_view()),
    path('api/update/<int:id>', views.CompanyUpdate.as_view()),

]