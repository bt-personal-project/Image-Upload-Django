from django.contrib import admin
from .models import HeroSection

class HeroAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "img_preview")
    list_display = ["heroTitle", "heroImg", "img_preview"]

# Register your models here.
admin.site.register(HeroSection, HeroAdmin)