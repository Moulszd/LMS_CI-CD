from django.db import models

from django.core.validators import FileExtensionValidator

from django.utils import timezone

##TODO: look up what gettext_lazzy is
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.TimeField(default=timezone.datetime.now())


class Category(BaseModel):
    category_name = models.TextField(max_length=80)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

# subtitle lang
class Course(BaseModel):
    class Course_type(models.TextChoices):
        recorded = 'REC', _('Recorded Course')
        live = 'LIV', _('Live Session')
        webinar = 'WEB', _('Webinar')
        track = 'TRA', _('Learning Track')

    class Language(models.TextChoices):
        arabic = 'AR', _('Arabic')
        english = 'EN', _('English')
        turkish = 'TR', _('Turkish')

    class Level(models.TextChoices):
        beginner = 'BEG', _('Beginner')
        intermediate = 'INT', _('Intermediate')
        advanced = 'ADV', _('Advanced')

    course_type = models.CharField(max_length=3, choices=Course_type, default=Course_type.recorded)

    title = models.TextField(max_length=80, blank=False, null=False, default='archived course')

    sub_title = models.TextField(max_length=120, blank=False, null=False, default='archived course')

    # course_thumb = models.ImageField(upload_to='course_thumbnails')

    # course_trailer = models.FileField(upload_to='course_trailer',
                                    #   null=True,
                                    #   validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    
    course_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    language = models.CharField(max_length=2, choices=Language, default=Language.arabic)

    duration = models.DurationField(help_text='HH:MM:SS')

    description = models.TextField(max_length=1000)

    price = models.IntegerField(blank=False, null=False, help_text='$$')

    def __str__(self):
        return self.title