from django.db import models

# Create your models here.
class HeroSection(models.Model):
    heroTitle = models.CharField(max_length=100)
    heroImg = models.ImageField(upload_to="herosection/media")