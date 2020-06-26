from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
	SUIT_CHOICES = (
		('diamonds','Diamonds'),
		('clubs', 'Clubs'),
		('spades', 'Spades'),
		('hearts', 'Hearts'),
		)	

	number = models.IntegerField()
	suit = models.CharField(max_length=50, choices=SUIT_CHOICES)

	def __str__(self):
		return str(self.number) + ' of ' + self.suit

class Hand(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cards = models.ManyToManyField(Card, blank=True)

class Game(models.Model):

	players = models.ManyToManyField(User, blank=True)
	cards = models.ManyToManyField(Card, blank=True)

