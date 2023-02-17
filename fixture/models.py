from django.db import models

# Create your models here.
class FixtureSection(models.Model):
    homeTeamImg = models.ImageField(upload_to='fixture/media')
    awayTeamImg = models.ImageField(upload_to='fixture/media')
    homeTeamTitle = models.CharField(max_length=50)
    awayTeamTitle = models.CharField(max_length=50)

class PremierLeagueTable(models.Model):
    teamName = models.CharField(max_length=50)
    mactchPlayed = models.IntegerField()
    winGame = models.IntegerField()
    drawGame = models.IntegerField()
    lossGame = models.IntegerField()
    totalPoints = models.IntegerField()
