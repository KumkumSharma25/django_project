from django.db import models

class House(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name

class Room(models.Model):
    title = models.CharField(max_length=100)
    furniture = models.CharField(max_length=100)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='my')

    def __str__(self):
        return self.title


# Create your models here.
