from diana.abstract.serializers import DynamicDepthSerializer, GenericSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from . import models
from diana.utils import get_fields, DEFAULT_FIELDS
from .models import *


class PlaceSerializer(DynamicDepthSerializer):

    class Meta:
        model = Place
        fields = get_fields(Place, exclude=DEFAULT_FIELDS+['min_year', 'max_year'])+ ['names', 'id']


class PlaceGeoSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Place
        fields = get_fields(Place, exclude=DEFAULT_FIELDS)+ ['names', 'id']
        geo_field = 'geometry'
        depth = 1


class TIFFImageSerializer(DynamicDepthSerializer):

    class Meta:
        model = Image
        fields = get_fields(Image, exclude=DEFAULT_FIELDS)+ ['id']


class VideoSerializer(DynamicDepthSerializer):

    class Meta:
        model = Video
        fields = get_fields(Video, exclude=DEFAULT_FIELDS)+ ['id']


class ObservationSerializer(DynamicDepthSerializer):

    class Meta:
        model = Observation
        fields = get_fields(Observation, exclude=DEFAULT_FIELDS)+ ['id']


class RePhotographySerializer(DynamicDepthSerializer):

    class Meta:
        model = RePhotography
        fields = get_fields(RePhotography, exclude=DEFAULT_FIELDS)+ ['id']
