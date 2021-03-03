from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from api import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
