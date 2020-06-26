from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Card, Hand, Game

def home(request):
	return render(request, 'home.html')

def game(request):
	player = request.user
	game = Game.objects.create()
	game.players.add(player)
	game.save()
	context = {
		'game': game,
		'player': player,
		'other_players': User.objects.all(),
	}

	return render(request, 'game.html', context),
	