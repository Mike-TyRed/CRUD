from django.db import models

# Create your models here.

class stadium(models.Model):
    stadium_id = models.AutoField(primary_key=True)
    stadium_name = models.CharField(max_length=100)
    stadium_location = models.CharField(max_length=100)
    stadium_capacity = models.IntegerField()
    stadium_image = models.ImageField(upload_to='stadiums')

    def __str__(self):
        return self.stadium_name

class team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    team_logo = models.ImageField(upload_to='teams')
    team_stadium = models.ForeignKey(stadium, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name

class player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=100)
    player_image = models.ImageField(upload_to='players')
    player_team = models.ForeignKey(team, on_delete=models.CASCADE)

    def __str__(self):
        return self.player_name