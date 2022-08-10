from django.db import models

# Create your models here.

class Tipo(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'types'

class Personaje(models.Model):

    name = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'personajes'


