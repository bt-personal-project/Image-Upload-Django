from django.db import models
from autoslug import AutoSlugField

class ImageUpload(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='homepage/media')
    
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)