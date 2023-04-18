from django.contrib import admin
from django.contrib.gis.db import models
from .models import *
from django.utils.html import format_html
from django.contrib.gis import admin
from django.utils.translation import gettext_lazy as _
from diana.utils import get_fields, DEFAULT_FIELDS, DEFAULT_EXCLUDE
from admin_auto_filters.filters import AutocompleteFilter
from rangefilter.filters import NumericRangeFilter
from django.contrib.admin import EmptyFieldListFilter
from django.conf import settings


DEFAULT_LONGITUDE =  10.5000
DEFAULT_LATITUDE  = 79.5000
DEFAULT_ZOOM = 8


# Register your models here.
@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Place)
class PlaceAdmin(admin.GISModelAdmin):

    fields              = get_fields(Place, exclude=['id'])
    readonly_fields     = [*DEFAULT_FIELDS]
    list_display = ['name', 'geometry', 'description', 'comment']
    search_fields = ['name']

    gis_widget_kwargs = {
        'attrs': {
            'default_lon' : DEFAULT_LONGITUDE,
            'default_lat' : DEFAULT_LATITUDE,
            'default_zoom' : DEFAULT_ZOOM,
        },
    }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['text']
    search_fields = ['text']


@admin.register(Focus)
class FocusAdmin(admin.GISModelAdmin):
    list_display = ['name', 'place', 'text']
    search_fields = ['name', 'text']


@admin.register(Image)
class ImageModel(admin.ModelAdmin):

    fields              = ['image_preview', *get_fields(Image, exclude=['id'])]
    readonly_fields     = ['iiif_file', 'uuid', 'image_preview', *DEFAULT_FIELDS]
    autocomplete_fields = ['creator', 'place', 'tag', 'focus']
    list_display = ['title', 'thumbnail_preview', 'creator', 'place', 'date', 'description']

    list_per_page = 10

    def image_preview(self, obj):
        return format_html(f'<img src="{settings.IIIF_URL}{obj.iiif_file}/full/full/0/default.jpg" height="300" />')
    
    def thumbnail_preview(self, obj):
        return format_html(f'<img src="{settings.IIIF_URL}{obj.iiif_file}/full/full/0/default.jpg" height="100" />')


@admin.register(RePhotography)
class RePhotographyAdmin(admin.ModelAdmin):
    list_display = ['old_image', 'new_image']


@admin.register(Video)
class VideoModel(admin.ModelAdmin):
    autocomplete_fields = ['creator', 'place', 'tag', 'focus']
    list_display = ['title', 'creator', 'place', 'link', 'date', 'description']

@admin.register(Observation)
class ObservationModel(admin.ModelAdmin):
    autocomplete_fields = ['creator', 'place', 'tag', 'focus']
    list_display = ['title', 'creator', 'place', 'date', 'description']


