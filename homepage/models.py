from django.db import models
from autoslug import AutoSlugField
from django.utils.html import mark_safe
from tinymce.models import HTMLField
from datetime import datetime, date, timezone

class ImageUpload(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField(default='description')
    description = HTMLField()
    image = models.ImageField(upload_to='homepage/media')

    date = models.DateField(auto_now_add=False, auto_now=True, blank=True)
    
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)

    def img_preview(self):
        return mark_safe(f'<img src="{self.image.url}" width="100" height="100" alt="IMG"/>')
    
    def __str__(self):
        # return  'Title ' + ': ' + self.title[:2] + '...' 
        return  'Title ' + ': ' + self.title
    
    class Meta:
        get_latest_by = 'id'

    

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)