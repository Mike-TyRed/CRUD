from django.db import models

# Create your models here.

class Team(models.Model):
    id_team = models.AutoField(primary_key=True)
    name_team = models.CharField(max_length=50)
    city_team = models.CharField(max_length=50)

    def __str__(self):
        return self.name_team

class Player(models.Model):
    id_player = models.AutoField(primary_key=True)
    name_player = models.CharField(max_length=50)
    age_player = models.IntegerField()
    team_player = models.CharField(max_length=50)

    def __str__(self):
        return self.name_player

class Stadium(models.Model):
    id_stadium = models.AutoField(primary_key=True)
    name_stadium = models.CharField(max_length=50)
    location_stadium = models.CharField(max_length=50)

    def __str__(self):
        return self.name_stadium