from django.shortcuts import render, redirect
from .models import Player, Team, Stadium

# Create your views here.

def main(request):
    return render(request, 'main.html', {})

def listPlayer(request):
    players = Player.objects.all()
    return render(request, 'player.html', {'players': players})

def registerPlayer(request):
    if request.method == 'POST':
        name_player = request.POST['name_player']
        age_player = request.POST['age_player']
        team_player = request.POST['team_player']
        player = Player(name_player=name_player, age_player=age_player, team_player=team_player)
        player.save()
    return redirect('player')

def editPlayer(request, id):
    player = Player.objects.get(id_player=id)
    return render(request, 'editPlayer.html', {'player': player})

def deletePlayer(request, id):
    player = Player.objects.get(id_player=id)
    player.delete()
    return redirect('player')

def updatePlayer(request, id):
    name_player = request.POST['name_player']
    age_player = request.POST['age_player']
    team_player = request.POST['team_player']
    
    player = Player.objects.get(id_player=id)
    player.name_player=name_player
    player.age_player=age_player
    player.team_player=team_player
    
    player.save()
    return redirect('player')

#-----------------------------------------------------------TEAMS

def listTeam(request):
    teams = Team.objects.all()
    return render(request, 'team.html', {'teams': teams})

def registerTeam(request):
    if request.method == 'POST':
        name_team = request.POST.get('name_team', False)
        city_team = request.POST['city_team']
        team = Team(name_team=name_team, city_team=city_team)
        team.save()
    return redirect('team')


def editTeam(request, id):
    team = Team.objects.get(id_team=id)
    return render(request, 'editTeam.html', {'team': team})

def deleteTeam(request, id):
    team = Team.objects.get(id_team=id)
    team.delete()
    return redirect('team')

def updateTeam(request, id):
    name_team = request.POST['name_team']
    city_team = request.POST['city_team']

    team = Team.objects.get(id_team=id)
    team.name_team=name_team
    team.city_team=city_team

    team.save()
    return redirect('team')

#-----------------------------------------------------------STADIUMS

def listStadium(request):
    stadiums = Stadium.objects.all()
    return render(request, 'stadium.html', {'stadiums': stadiums})

def registerStadium(request):
    if request.method == 'POST':
        name_stadium = request.POST['name_stadium']
        location_stadium = request.POST['location_stadium']
        stadium = Stadium(name_stadium=name_stadium, location_stadium=location_stadium)
        stadium.save()
    return redirect('stadium')

def editStadium(request, id):
    stadium = Stadium.objects.get(id_stadium=id)
    return render(request, 'editStadium.html', {'stadium': stadium})

def deleteStadium(request, id):
    stadium = Stadium.objects.get(id_stadium=id)
    stadium.delete()
    return redirect('stadium')

def updateStadium(request):
    name_stadium = request.POST['name_stadium']
    location_stadium = request.POST['location_stadium']
    
    stadium = Stadium.objects.get(id_stadium=id)
    stadium.name_stadium=name_stadium
    stadium.location_stadium=location_stadium

    stadium.save()
    return redirect('stadium')