# from django.db import models
from django.contrib.gis.db import models
import diana.abstract.models as abstract
from django.utils.translation import gettext_lazy as _
# Create your models here.

# Place
class Place(abstract.AbstractBaseModel):
    
    placename = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Placename"), help_text=_("Free-form, non-indexed placename of the site."))
    geometry = models.GeometryField(verbose_name=_("geometry"), blank=True, null=True)
    description = models.TextField(null=True, blank=True, verbose_name=_("description"))
    comment  = models.TextField(null=True, blank=True, verbose_name=_("comment"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Placename")

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



# Tag 
class Tag(abstract.AbstractTagModel):

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Focus(abstract.AbstractBaseModel):
    place = models.GeometryField(blank=True, null=True)
    text = models.TextField(null=True, blank=True)


# Photo
class Image(abstract.AbstractTIFFImageModel):

    title = models.CharField(max_length=1024, null=True, blank=True, verbose_name=_("general.title"))
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, blank=True, related_name="photographer")
    placename   = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE, related_name="image_location")
    description = models.TextField(null=True, blank=True, help_text=("Descriptive text about the the motif"))
    date = models.DateField(null=True, blank=True, help_text=("Date of photography"))
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("tags"))
    focus = models.ForeignKey(Focus, null=True, blank=True, on_delete=models.CASCADE, help_text=("what is documented, also a place on a map"))

    def __str__(self) -> str:
        return f"{self.title}"

# Video
class Video(abstract.AbstractBaseModel):
    title = models.CharField(max_length=1024, null=True, blank=True, verbose_name=_("general.title"))
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, blank=True, related_name="director")
    placename  = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE, related_name="video_location")
    link = models.URLField(blank=True, null=True, help_text=("Video link in GU Play"))
    description = models.TextField(null=True, blank=True, help_text=("Descriptive text about the the motif"))
    date = models.DateField(null=True, blank=True, help_text=("Date of video"))
    focus = models.ForeignKey(Focus, null=True, blank=True, on_delete=models.CASCADE, help_text=("what is documented, also a place on a map"))
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("tags"))

    def __str__(self) -> str:
        return f"{self.title}"

# Observation
class Observation(abstract.AbstractBaseModel):
    title = models.CharField(max_length=1024, null=True, blank=True, verbose_name=_("general.title"))
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, blank=True, related_name="researcher")
    placename   = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE, related_name="research_location")
    description = models.TextField(null=True, blank=True, help_text=("Descriptive text about the the motif"))
    date = models.DateField(null=True, blank=True, help_text=("Date of tacking note"))
    focus = models.ForeignKey(Focus, null=True, blank=True, on_delete=models.CASCADE, help_text=("what is documented, also a place on a map"))
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("tags"))

    def __str__(self) -> str:
        return f"{self.title}"        

# 3D models
# We don't have any information about this type of data.

# Re-photography
class RePhotography(abstract.AbstractBaseModel):
    old_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="old_image")
    new_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="new_image")