from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    nombre_carousel = models.CharField(max_length=30)
    caracteristicas_carousel = models.CharField(max_length=50)
    nombre = models.CharField(max_length=15)
    caracteristicas = models.CharField(max_length=250)
    editor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='editor')

    def __str__(self):
        return f"{self.id} -- {self.nombre_carousel} -- {self.caracteristicas_carousel}"


