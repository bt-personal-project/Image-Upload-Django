from django.contrib import admin
from .models import FixtureSection, PremierLeagueTable

class PremierLeagueTableAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = ["teamName", "mactchPlayed", "winGame", "drawGame", "lossGame", "totalPoints"]

class FixtureAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "img_preview")
    list_display = ["homeTeamTitle", "awayTeamTitle"]

# Register your models here.
admin.site.register(FixtureSection, FixtureAdmin)
admin.site.register(PremierLeagueTable, PremierLeagueTableAdmin)