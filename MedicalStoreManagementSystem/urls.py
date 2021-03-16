

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


from django.conf import settings


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('Company.urls')),
    path('medicine/', include('Medicine.urls')),
    path('customer/', include('Customer.urls')),
    path('employee/', include('Employee.urls')),
    path('api/gettoken/', TokenObtainPairView.as_view(), name="gettoken"),
    path('api/resfresh_token/', TokenRefreshView.as_view(), name="refresh_token"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





