from unittest.mock import DEFAULT
from rest_framework import viewsets
from . import models, serializers

from diana.abstract.views import DynamicDepthViewSet, GeoViewSet
from diana.abstract.models import get_fields, DEFAULT_FIELDS


class PlaceViewSet(DynamicDepthViewSet):
    
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    filterset_fields = get_fields(models.Place, exclude=DEFAULT_FIELDS + ['geometry'])
    search_fields = ['placename']


class PlaceGeoViewSet(GeoViewSet):

    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceGeoSerializer
    filterset_fields = get_fields(models.Place, exclude=DEFAULT_FIELDS + ['geometry'])
    search_fields = ['placename']
    bbox_filter_field = 'tag'
    bbox_filter_include_overlapping = True


# Create your views here.
class IIIFImageViewSet(DynamicDepthViewSet):
    """
    retrieve:
    Returns a single image instance.

    list:
    Returns a list of all the existing images in the database, paginated.

    count:
    Returns a count of the existing images after the application of any filter.
    """
    
    queryset = models.Image.objects.all()
    serializer_class = serializers.TIFFImageSerializer
    filterset_fields = get_fields(models.Image, exclude=DEFAULT_FIELDS + ['iiif_file', 'file'])


class VideoViewSet(DynamicDepthViewSet):
    
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
    filterset_fields = get_fields(models.Video, exclude=DEFAULT_FIELDS)


class ObservationViewSet(DynamicDepthViewSet):
    
    queryset = models.Observation.objects.all()
    serializer_class = serializers.ObservationSerializer
    filterset_fields = get_fields(models.Observation, exclude=DEFAULT_FIELDS)

class RePhotographyViewSet(DynamicDepthViewSet):
    
    queryset = models.RePhotography.objects.all()
    serializer_class = serializers.RePhotographySerializer
    filterset_fields = get_fields(models.RePhotography, exclude=DEFAULT_FIELDS)