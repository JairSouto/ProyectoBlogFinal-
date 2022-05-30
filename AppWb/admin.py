from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cursos)
admin.site.register(Asociados)
admin.site.register(Equipos)
admin.site.register(Avatar)
