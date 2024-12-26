from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    username = models.CharField(max_length=100)
    team = models.ForeignKey(Team, related_name='users', on_delete=models.CASCADE)

class Game(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.TextField()
    dealer = models.CharField(max_length=100)
    team = models.ForeignKey(Team, related_name='games', on_delete=models.CASCADE)

class Card(models.Model):
    game = models.ForeignKey(Game, related_name='cards', on_delete=models.CASCADE)
    player_name = models.CharField(max_length=100)
    vote_number = models.IntegerField()
