from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from society.views import PlotViewset, VideoViewset

router = DefaultRouter()

# router.register('city', CityViewset, basename="api")
# router.register('society', SocietyViewset, basename="api")
router.register('plot', PlotViewset, basename="api")
router.register('video', VideoViewset, basename="api2")

urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
]