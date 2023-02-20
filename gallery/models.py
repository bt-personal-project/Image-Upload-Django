from django.db import models
from datetime import date
from django.utils.html import mark_safe

class GallerySection(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="gallery/media")
    date = models.DateTimeField()

    def img_preview(self):
        return mark_safe(f'<img src="{self.image.url}" width="100px" height="100px" syle="object-fit: cover;">')
