from django.db import models

# Create your models here.
class HeroD(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f'{self.title} by {self.author}'