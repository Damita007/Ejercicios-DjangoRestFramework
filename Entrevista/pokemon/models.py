from django.db import models

# Create your models here.

class Tipo(models.Model):
    GRASS = 'GRASS'
    FIRE = 'FIRE'
    WATER = 'WATER'
    BUG = 'BUG'
    NORMAL = 'NORMAL'
    POISON = 'POISON'
    ELECTRIC = 'ELECTRIC'
    GROUND = 'GROUND'
    FAIRY = 'FAIRY'
    FIGHTING = 'FIGHTING'
    PSYCHIC = 'PSYCHIC'
    NAME_CHOICES=[
    ('GRASS', 'grass'),
    ('FIRE', 'fire'),
    ('WATER', 'water'),
    ('BUG', 'bug'),
    ('NORMAL', 'normal'),
    ('POISON', 'poison'),
    ('ELECTRIC', 'electric'),
    ('GROUND', 'ground'),
    ('FAIRY', 'fairy'),
    ('FIGHTING', 'fighting'),
    ('PSYCHIC', 'psychic')
    ]
    name = models.CharField(max_length=20, choices=NAME_CHOICES, blank=False, default=GRASS)

    class Meta:
        db_table = 'types'

class Personaje(models.Model):

    name = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'personajes'


