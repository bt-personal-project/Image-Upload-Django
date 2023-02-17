from django.contrib import admin
from .models import FixtureSection, PremierLeagueTable

class PremierLeagueTableAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = ["teamName", "mactchPlayed", "winGame", "drawGame", "lossGame", "totalPoints"]

# Register your models here.
admin.site.register(FixtureSection)
admin.site.register(PremierLeagueTable, PremierLeagueTableAdmin)