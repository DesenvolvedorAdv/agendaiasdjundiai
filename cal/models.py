from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from home.models import Sala
from django.conf import settings

LISTA_DEPARTAMENTO = (('ANCIONATO', 'Ancionato'),('SECRETARIA','Secretaria'))

# Create your models here.
class Usuario(AbstractBaseUser):
    departamento = models.CharField(max_length=255,choices=LISTA_DEPARTAMENTO)

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    # sala = models.ManyToManyField(Sala)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, null=True)
    aprovada = models.BooleanField(default=False)
    cor = models.CharField(max_length=7, null=True, blank=True)
    class Meta:
        db_table = "tblevento"
