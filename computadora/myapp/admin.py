from django.contrib import admin
from .models import *


#registramos cada uno de nuestros modelos o tablas de la base de datos 
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Oficina)
admin.site.register(Departamento)
admin.site.register(LugarReparacion)
admin.site.register(Usuario)
admin.site.register(Equipo)
admin.site.register(Estado)
admin.site.register(Auditoria)
admin.site.register(Procesador)
admin.site.register(SistemaOperativo)
admin.site.register(MantenimientoPreventivo)
admin.site.register(Ups)
admin.site.register(DetalleLectUps)
admin.site.register(AlarmaSistemas)
admin.site.register(Ats)
admin.site.register(DetalleAts)
admin.site.register(AireDatacenter)
admin.site.register(DetalleAire)
admin.site.register(Protocolo)


