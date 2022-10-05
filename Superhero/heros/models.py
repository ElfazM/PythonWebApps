from django.db import models

class Character(models.Model):
    CharacterName = models.CharField(max_length=200)
    Creator = models.CharField(max_length=200)
    Power = models.TextField()