from django.urls import path, include
from rest_framework import routers
from . import views
import diana.utils as utils


router = routers.DefaultRouter()
endpoint = utils.build_app_endpoint("rephotography")
documentation = utils.build_app_api_documentation("rephotography", endpoint)

router.register(rf'{endpoint}/place', views.PlaceGeoViewSet, basename='place')
router.register(rf'{endpoint}/image', views.IIIFImageViewSet, basename='image')
# router.register(rf'{endpoint}/video', views.IIIFImageViewSet, basename='image')
# router.register(rf'{endpoint}/observation', views.IIIFImageViewSet, basename='image')
# router.register(rf'{endpoint}/rephotography', views.IIIFImageViewSet, basename='image')

urlpatterns = [
    path('', include(router.urls)),

]