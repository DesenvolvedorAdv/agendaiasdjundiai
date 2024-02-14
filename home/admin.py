from django.contrib import admin
from .models import Horario, Sala, Events


# Register your models here.
admin.site.register(Horario)
admin.site.register(Events)
admin.site.register(Sala)
