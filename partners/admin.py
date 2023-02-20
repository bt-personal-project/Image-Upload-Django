from django.contrib import admin
from .models import Partners

class PartnersAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "img_preview")
    list_display = ["title", "img_preview", "image", "date"]

admin.site.register(Partners, PartnersAdmin)