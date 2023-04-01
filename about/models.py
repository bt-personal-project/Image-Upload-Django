from django.db import models
from tinymce.models import HTMLField
from django.utils.html import mark_safe


class AboutSection(models.Model):
    title = models.CharField(max_length=50)
    description = HTMLField()
    image = models.ImageField(upload_to="about/media")

    def img_preview(self):
        return mark_safe(f'<img src="{self.image.url}" width="100px" height="100px" style="object-fit: cover;">')
