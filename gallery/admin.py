from django.contrib import admin
from .models import GallerySection

class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = ["title", "img_preview", "image", "date"]

admin.site.register(GallerySection, GalleryAdmin)