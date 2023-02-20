from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class FixtureSection(models.Model):
    homeTeamImg = models.ImageField(upload_to='fixture/media')
    awayTeamImg = models.ImageField(upload_to='fixture/media')
    homeTeamTitle = models.CharField(max_length=50)
    awayTeamTitle = models.CharField(max_length=50)

    def __str__(self):
        return "Fixture"
    
    def img_preview(self):
        return mark_safe(f'<img src="{self.homeTeamImg.url}" height="50px" width="50px" style="object-fit: contain;"> VS <img src="{self.awayTeamImg.url}" height="50px" width="50px" style="object-fit: contain;">')

class PremierLeagueTable(models.Model):
    teamName = models.CharField(max_length=50)
    mactchPlayed = models.IntegerField()
    winGame = models.IntegerField()
    drawGame = models.IntegerField()
    lossGame = models.IntegerField()
    totalPoints = models.IntegerField()

    def __str__(self):
        # return self.teamName + ' ' + str(self.mactchPlayed)
        return self.teamName


