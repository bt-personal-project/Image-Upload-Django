from django.contrib import admin
from .models import AboutSection

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "img_preview",)
    list_display = ["title", "description", "image", "img_preview"]

# Register your models here.
admin.site.register(AboutSection, AboutAdmin)