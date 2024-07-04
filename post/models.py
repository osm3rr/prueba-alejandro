from django.db import models

# Create your models here.

class Publicaciones(models.Model):

    titulo= models.CharField(max_length=40)
    descripcion=models.TextField()