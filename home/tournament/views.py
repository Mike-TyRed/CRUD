from django.shortcuts import render, redirect
from .models import team
from .models import stadium
from .models import player

# Create your views here.

def stadium_list(request):
    stadiums = stadium.objects.all()
    return render(request, 'stadium.html', {'stadiums': stadiums})

def team_list(request):
    teams = team.objects.all()
    return render(request, 'team.html', {'teams': teams})

def player_list(request):
    players = player.objects.all()
    return render(request, 'player.html', {'players': players})

def registerStadium(request):
    stadium_name = request.POST['stadium_name']
    stadium_location = request.POST['stadium_location']
    stadium_capacity = request.POST['stadium_capacity']

    stadium.objects.create(stadium_name=stadium_name, stadium_location=stadium_location, stadium_capacity=stadium_capacity)

    return redirect('stadium')

def deleteStadium(request, id):
    stadium.objects.filter(id=id).delete()
    return redirect('stadium')

def editStadium(request, id):
    stadium_name = request.POST['stadium_name']
    stadium_location = request.POST['stadium_location']
    stadium_capacity = request.POST['stadium_capacity']

    stadium.objects.filter(id=id).update(stadium_name=stadium_name, stadium_location=stadium_location, stadium_capacity=stadium_capacity)

    return redirect('stadium')