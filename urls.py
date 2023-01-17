from django.urls import path, include
from rest_framework import routers
from . import views
import diana.utils as utils

router = routers.DefaultRouter()
endpoint = utils.build_app_endpoint("rephotography")
documentation = utils.build_app_api_documentation("rephotography", endpoint)

urlpatterns = [
    path('', include(router.urls)),

]