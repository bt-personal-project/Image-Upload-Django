from django.contrib import admin
from .models import ContactSection
from .models import ContactDetails

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ("id", )
    list_display = ["title"]

class ContactDetail(admin.ModelAdmin):
    readonly_fields = ("id", )
    list_display = ["detailTitle", "detailDescription"]

admin.site.register(ContactSection, ContactAdmin)
admin.site.register(ContactDetails, ContactDetail)