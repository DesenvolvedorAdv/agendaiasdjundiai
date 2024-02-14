from django.db import models

HORARIOS = [
    ("1","09:30 - 12:00"),
    ("2","12:00 - 15:30"),
    ("3","15:30 - 19:30"),
    ("4","19:30 - 21:30"),
    ("5","15:30 - 21:30")]

class Horario(models.Model):
    name = models.CharField(max_length=55, null=True, blank=True, choices=HORARIOS)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    class Meta:
        db_table = "tblhorarios"

class Sala(models.Model):
    name = models.CharField(max_length=15, null=True, blank=True)
    thumb = models.ImageField(upload_to='thumb_salas')
    tipo = models.CharField(max_length=15, null=True, blank=True, )
    horarios = models.ManyToManyField(Horario)
    class Meta:
        db_table = "tblsala"


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    # # departamento =  models.CharField(max_length=50,choices=LISTA_DEPARTAMENTO)
    # usuario =  models.ForeignKey(Usuario, on_delete=models.CASCADE)
    sala = models.ManyToManyField(Sala)
    aprovada = models.BooleanField(default=False)
    class Meta:
        db_table = "tblevents"
