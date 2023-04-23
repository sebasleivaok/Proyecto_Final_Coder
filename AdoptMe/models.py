from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    nombre_carousel = models.CharField(max_length=30)
    caracteristicas_carousel = models.CharField(max_length=50)
    nombre = models.CharField(max_length=15)
    caracteristicas = models.CharField(max_length=250)
    editor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='editor')
    imagen = models.ImageField(upload_to="posts")
    creado_el = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.id} -- {self.nombre_carousel} -- {self.caracteristicas_carousel}"

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    instagram = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="profiles")

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="destinatario")



