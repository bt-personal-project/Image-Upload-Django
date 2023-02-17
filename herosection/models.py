from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class HeroSection(models.Model):
    heroTitle = models.CharField(max_length=100)
    heroImg = models.ImageField(upload_to="herosection/media")

    def __str__(self):
        return self.heroTitle

    def img_preview(self):
        return mark_safe(f'<img src="{self.heroImg.url}" width="100" height="100" alt="HERO">')
