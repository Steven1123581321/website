from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Cv2(models.Model):
    welcome_title = models.TextField()
    welcome_text = RichTextUploadingField(
        blank=True,
        null=True,
    )
    video = RichTextUploadingField(
        blank=True,
        null=True,
        config_name="cv",
        external_plugin_resources=[
            (
                "youtube",
                "/static/youtube/",
                "plugin.js",
            )
        ],
    )
