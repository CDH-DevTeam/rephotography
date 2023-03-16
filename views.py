from unittest.mock import DEFAULT
from . import models, serializers
from django.db.models import Prefetch, Q
from diana.abstract.views import DynamicDepthViewSet, GeoViewSet
from diana.abstract.models import get_fields, DEFAULT_FIELDS


class PlaceViewSet(DynamicDepthViewSet):
    serializer_class = serializers.PlaceSerializer
    filterset_fields = get_fields(models.Place, exclude=DEFAULT_FIELDS + ['geometry'])
    search_fields = ['placename']

    def dispatch(self, request, *args, **kwargs):
        model_name = request.GET.get('type')
        if model_name == 'image':
            self.model = models.Image
        elif model_name == 'video':
            self.model = models.Video
        elif model_name == 'observation':
            self.model = models.Observation
        return super(PlaceViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = models.Place.objects.all()
        model_type = self.request.query_params.get('type')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if model_type:
            objects_type = self.model.objects.all()
            if start_date and end_date:
                objects_type = objects_type.filter(date__year__gte=start_date, date__year__lte=end_date)
            elif start_date:
                objects_type = objects_type.filter(date__year=start_date)
            queryset = models.Place.objects.all().filter(id__in=list(objects_type.values_list('place', flat=True)))
        return queryset

class PlaceGeoViewSet(GeoViewSet):

    # queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceGeoSerializer
    filterset_fields = get_fields(models.Place, exclude=DEFAULT_FIELDS + ['geometry'])
    search_fields = ['placename']
    bbox_filter_field = 'geometry'
    bbox_filter_include_overlapping = True

    def dispatch(self, request, *args, **kwargs):
        model_name = request.GET.get('type')
        if model_name == 'image':
            self.model_type = models.Image
        elif model_name == 'video':
            self.model_type = models.Video
        elif model_name == 'observation':
            self.model_type = models.Observation
        return super(PlaceGeoViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = models.Place.objects.all()
        model_type_name = self.request.query_params.get('type')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if model_type_name:
            objects_type = self.model_type.objects.all()
            if start_date and end_date:
                objects_type = objects_type.filter(date__year__gte=start_date, date__year__lte=end_date)
            elif start_date:
                objects_type = objects_type.filter(date__year=start_date)
            queryset = models.Place.objects.all().filter(id__in=list(objects_type.values_list('place', flat=True)))
        return queryset

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
