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

# Register your models here.
@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Place)
class PlaceAdmin(admin.GISModelAdmin):
    list_display = ['placename', 'geometry', 'description', 'comment']
    search_fields = ['placename']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['text']
    search_fields = ['text']


@admin.register(Focus)
class FocusAdmin(admin.GISModelAdmin):
    list_display = ['place', 'text']
    search_fields = ['text']


@admin.register(Image)
class ImageModel(admin.ModelAdmin):
    autocomplete_fields = ['creator', 'placename', 'tag', 'focus']
    list_display = ['title', 'creator', 'placename', 'date', 'description']

    list_per_page = 10

    def image_preview(self, obj):
        return format_html(f'<img src="{settings.ORIGINAL_URL}/{obj.file}" height="300" />')

@admin.register(RePhotography)
class RePhotographyAdmin(admin.ModelAdmin):
    list_display = ['old_image', 'new_image']


@admin.register(Video)
class VideoModel(admin.ModelAdmin):
    autocomplete_fields = ['creator', 'placename', 'tag', 'focus']
    list_display = ['title', 'creator', 'placename', 'link', 'date', 'description']

@admin.register(Observation)
class ObservationModel(admin.ModelAdmin):
    autocomplete_fields = ['creator', 'placename', 'tag', 'focus']
    list_display = ['title', 'creator', 'placename', 'date', 'description']


