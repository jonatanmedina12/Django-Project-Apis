from django.contrib import admin
from .models import Inmueble, Empresa, Comentario

# Register your models here.
admin.site.register(Inmueble)
admin.site.register(Empresa)
admin.site.register(Comentario)
