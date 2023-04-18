# from django.db import models
from django.contrib.gis.db import models
import diana.abstract.models as abstract
from django.utils.translation import gettext_lazy as _
from diana.storages import OriginalFileStorage
from diana.abstract.models import get_original_path
# Create your models here.


# Tag 
class Tag(abstract.AbstractTagModel):

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

# Place
class Place(abstract.AbstractBaseModel):
    
    name = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("name"), help_text=_("Free-form, non-indexed placename of the site."))
    geometry = models.GeometryField(verbose_name=_("geometry"), blank=True, null=True)
    description = models.TextField(null=True, blank=True, verbose_name=_("description"))
    comment  = models.TextField(null=True, blank=True, verbose_name=_("comment"))
    tag = models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"))
    min_year = models.DateField(blank=True, null=True)
    max_year = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Place")

# Creator
class Creator(abstract.AbstractBaseModel):
    # A photographer, or creator of an observtion

    name = models.CharField(max_length=256, unique=True, verbose_name=_("name"), help_text=_("Free-form name of the creator, photographer or researcher."))
    # add role like photographer, film maker, researcher ...

    class Meta:
        verbose_name = _("Creator")
        verbose_name_plural = _("Creators")

    def __str__(self) -> str:
        return self.name



class Focus(abstract.AbstractBaseModel):
    name = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("name"))
    place = models.GeometryField(verbose_name=_("geometry"), blank=True, null=True)
    text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Focus")
        verbose_name_plural = _("Focuses")

    def __str__(self) -> str:
        return f"{self.name}"


# Photo
class Image(abstract.AbstractTIFFImageModel):

    title = models.CharField(max_length=1024, null=True, blank=True, verbose_name=_("general.title"))
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, null=True, blank=True, related_name="photographer")
    place   = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE, related_name="image_location")
    description = models.TextField(null=True, blank=True, help_text=("Descriptive text about the the motif"))
    date = models.DateField(null=True, blank=True, help_text=("Date of photography"))
    tag = models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"))
    focus = models.ForeignKey(Focus, null=True, blank=True, on_delete=models.CASCADE, help_text=("what is documented, also a place on a map"))

    
    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self) -> str:
        return f"{self.title}"

# Video
class Video(abstract.AbstractBaseModel):
    title = models.CharField(max_length=1024, null=True, blank=True, verbose_name=_("general.title"))
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, null=True, blank=True, related_name="director")
    place  = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE, related_name="video_location")
    link = models.URLField(blank=True, null=True, help_text=("Video link in GU Play"))
    description = models.TextField(null=True, blank=True, help_text=("Descriptive text about the the motif"))
    date = models.DateField(null=True, blank=True, help_text=("Date of video"))
    focus = models.ForeignKey(Focus, null=True, blank=True, on_delete=models.CASCADE, help_text=("what is documented, also a place on a map"))
    tag = models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"))

    def __str__(self) -> str:
        return f"{self.title}"

# Observation
class Observation(abstract.AbstractBaseModel):
    title = models.CharField(max_length=1024, null=True, blank=True, verbose_name=_("general.title"))
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, null=True, blank=True, related_name="researcher")
    document = models.FileField(null=True, blank=True, storage=OriginalFileStorage, upload_to=get_original_path, verbose_name=_("general.file"))
    place   = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE, related_name="research_location")
    description = models.TextField(null=True, blank=True, help_text=("Descriptive text about the the motif"))
    date = models.DateField(null=True, blank=True, help_text=("Date of tacking note"))
    focus = models.ForeignKey(Focus, null=True, blank=True, on_delete=models.CASCADE, help_text=("what is documented, also a place on a map"))
    tag = models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"))

    def __str__(self) -> str:
        return f"{self.title}"        

# 3D models
# We don't have any information about this type of data.

# Re-photography
class RePhotography(abstract.AbstractBaseModel):
    title = models.CharField(max_length=1024, null=True, blank=True, verbose_name=_("general.title"))
    old_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="old_image")
    new_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="new_image")
    tag = models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"))

    def __str__(self) -> str:
        return f"{self.title}"