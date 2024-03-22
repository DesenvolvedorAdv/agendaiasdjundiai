from django.contrib import admin
from .models import Horario, Sala, Events, Faq


# Register your models here.
admin.site.register(Horario)
admin.site.register(Events)
admin.site.register(Sala)
admin.site.register(Faq)
