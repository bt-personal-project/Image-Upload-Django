from django.db import models
from tinymce.models import HTMLField

class ContactSection(models.Model):
    title = models.CharField(max_length=20)

class ContactDetails(models.Model):
    detailTitle = models.CharField(max_length=50)
    detailDescription = HTMLField()

