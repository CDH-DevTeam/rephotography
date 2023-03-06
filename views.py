from unittest.mock import DEFAULT
from . import models, serializers
from django.db.models import Count, Q
from diana.abstract.views import DynamicDepthViewSet, GeoViewSet
from diana.abstract.models import get_fields, DEFAULT_FIELDS
from django.contrib.postgres.aggregates import ArrayAgg


class PlaceViewSet(DynamicDepthViewSet):

    # queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    filterset_fields = get_fields(models.Place, exclude=DEFAULT_FIELDS + ['geometry'])
    search_fields = ['placename']

    def get_queryset(self):
        model_name = str(self.request.query_params.get('q'))
        start_date = self.request.query_params.get('s')
        end_date = self.request.query_params.get('e')
        queryset = ''
        if model_name in 'image':
            queryset = models.Place.objects.all().filter(id__in=list(models.Image.objects.values_list('place', flat=True)))\
            .filter(min_year__year= start_date)\
            .filter(max_year__year= end_date)\
            .filter(Q(min_year__year= start_date) & Q(max_year__year= end_date))
        elif model_name in 'video':
            queryset = models.Place.objects.all().filter(id__in=list(models.Video.objects.values_list('place', flat=True)))
        elif model_name in 'observation':
            queryset = models.Place.objects.all().filter(id__in=list(models.Observation.objects.values_list('place', flat=True)))
        return queryset




class PlaceGeoViewSet(GeoViewSet):

    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceGeoSerializer
    filterset_fields = get_fields(models.Place, exclude=DEFAULT_FIELDS + ['geometry'])
    search_fields = ['placename']
    bbox_filter_field = 'geometry'
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
