from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe

class Partners(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="partners/media")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def img_preview(self):
        return mark_safe(f'<img src="{self.image.url}" width="100px" height="100px" alt="PREVIEW" style="object-fit: contain;">')