from django.contrib import admin
from .models import ImageUpload
from .models import News

class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register your models here.
admin.site.register(ImageUpload, ImageAdmin)
admin.site.register(News)