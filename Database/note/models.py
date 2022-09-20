from django.db import models

# Create your models here.build python models 
# have to first allow all hosts 
# migrate database


class Note(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):  
        return f'{self.pk}. {self.title} - {self.author}'  #how object will be formated 