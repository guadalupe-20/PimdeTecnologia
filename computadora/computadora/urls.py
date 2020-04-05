"""computadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 


from django.contrib import admin
from django.urls import include, path
from myapp import views# se importan todas las vistas creadas por el usuario
# equi esta el detalle de vada una de las urls necesarias para que el sistema funcione 
urlpatterns = [
    path('admin/', admin.site.urls),# url del administrador 
    path('', views.home, name='home'),# url para mostrar el login del sistema 
    path('login/', views.procesar_login, name="login"),
    path('logout/', views.salir, name="salir"),# url para salir del sistema 
    path('menu/', views.menu, name="menu"), # url que muestra el menu del sistema 
    path('reportetotal/', views.reportetotal, name="reportetotal"), # url que da acceso a los reportes del sistema en ul menu 
    
    path('trasladoequipos/', views.trasladoequipos, name="trasladoequipos"),  # url que da acceso a los reportes del sistema 
 
    # urls necesarias para mostrar todo lo referente a las oficinas que se agregan, actualizan, editar y el listado de las misma 
    path('oficina/', views.oficina, name="oficina"),
    path('oficinalista/', views.oficinalista, name="oficinalista"),
    path('guardar-oficina/', views.guardar_oficina, name="guardar_oficina"),
    path('guardar-oficina/<int:id>/', views.guardar_oficina, name="actualizar_oficina"),
    path('oficina/<int:id>/eliminar/', views.eliminar_oficina, name="eliminar_oficina"),
    path('oficina/<int:id>/editar/', views.editar_oficina, name="editar_oficina"),

    # urls necesarias para mostrar todo lo referente a los departamanetos  que se agregan, actualizan, editar y el listado de las misma 
    path('departamento/', views.departamento, name="departamento"),
    path('departamentolista/', views.departamentolista, name="departamentolista"),
    path('guardar-departamento/', views.guardar_departamento, name="guardar_departamento"),
    path('guardar-departamento/<int:id>/', views.guardar_departamento, name="actualizar_departamento"),
    path('departamento/<int:id>/eliminar/', views.eliminar_departamento, name="eliminar_departamento"),
    path('departamento/<int:id>/editar/', views.editar_departamento, name="editar_departamento"),

   # urls necesarias para mostrar todo lo referente a las marcas que se agregan, actualizan, editar y el listado de las misma 
    path('marca/', views.marca, name="marca"),
    path('marcalista/', views.marcalista, name="marcalista"),
    path('guardar-marca/', views.guardar_marca, name="guardar_marca"),
    path('guardar-marca/<int:id>/', views.guardar_marca, name="actualizar_marca"),
    path('dmarca/<int:id>/eliminar/', views.eliminar_marca, name="eliminar_marca"),
    path('marca/<int:id>/editar/', views.editar_marca, name="editar_marca"),

   # urls necesarias para mostrar todo lo referente a las modelos que se agregan, actualizan, editar y el listado de las misma 
    path('modelo/', views.modelo, name="modelo"),
    path('modelolista/', views.modelolista, name="modelolista"),
    path('guardar-modelo/', views.guardar_modelo, name="guardar_modelo"),
    path('guardar-modelo/<int:id>/', views.guardar_modelo, name="actualizar_modelo"),
    path('modelo/<int:id>/eliminar/', views.eliminar_modelo, name="eliminar_modelo"),
    path('modelo/<int:id>/editar/', views.editar_modelo, name="editar_modelo"),

   # urls necesarias para mostrar todo lo referente a las estados que se agregan, actualizan, editar y el listado de las misma 
    path('estado/', views.estado, name="estado"),
    path('estadolista/', views.estadolista, name="estadolista"),
    path('guardar-estado/', views.guardar_estado, name="guardar_estado"),
    path('guardar-estado/<int:id>/', views.guardar_estado, name="actualizar_estado"),
    path('estado/<int:id>/eliminar/', views.eliminar_estado, name="eliminar_estado"),
    path('estado/<int:id>/editar/', views.editar_estado, name="editar_estado"),

   # urls necesarias para mostrar todo lo referente a los lugares de reparacion  que se agregan, actualizan, editar y el listado de las misma 
    path('lugarreparacion/', views.lugarreparacion, name="lugarreparacion"),
    path('lugarreparacionlista/', views.lugarreparacionlista, name="lugarreparacionlista"),
    path('guardar-lugarreparacion/', views.guardar_lugarreparacion, name="guardar_lugarreparacion"),
    path('guardar-lugarreparacion/<int:id>/', views.guardar_lugarreparacion, name="actualizar_lugarreparacion"),
    path('lugarreparacion/<int:id>/eliminar/', views.eliminar_lugarreparacion, name="eliminar_lugarreparacion"),
    path('lugarreparacion/<int:id>/editar/', views.editar_lugarreparacion, name="editar_lugarreparacion"),

   # urls necesarias para mostrar todo lo referente a los usuarios que se agregan, actualizan, editar y el listado de las misma 
    path('usuario/', views.usuario, name="usuario"),
    path('usuariolista/', views.usuariolista, name="usuariolista"),
    path('guardar-usuario/', views.guardar_usuario, name="guardar_usuario"),
    path('guardar-usuario/<int:id>/', views.guardar_usuario, name="actualizar_usuario"),
    path('usuario/<int:id>/eliminar/', views.eliminar_usuario, name="eliminar_usuario"),
    path('usuario/<int:id>/editar/', views.editar_usuario, name="editar_usuario"),

   # urls necesarias para mostrar todo lo referente a las auditorias que se agregan, actualizan, editar y el listado de las misma 
    path('auditoria/', views.auditoria, name="auditoria"),
    path('auditorialista/', views.auditorialista, name="auditorialista"),
    path('guardar-auditoria/', views.guardar_auditoria, name="guardar_auditoria"),
    path('guardar-auditoria/<int:id>/', views.guardar_auditoria, name="actualizar_auditoria"),
    path('auditoria/<int:id>/eliminar/', views.eliminar_auditoria, name="eliminar_auditoria"),
    path('auditoria/<int:id>/editar/', views.editar_auditoria, name="editar_auditoria"),

   # urls necesarias para mostrar todo lo referente a los procesadores que se agregan, actualizan, editar y el listado de las misma 
    path('procesador/', views.procesador, name="procesador"),
    path('procesadorlista/', views.procesadorlista, name="procesadorlista"),
    path('guardar-procesador/', views.guardar_procesador, name="guardar_procesador"),
    path('guardar-procesador/<int:id>/', views.guardar_procesador, name="actualizar_procesador"),
    path('procesador/<int:id>/eliminar/', views.eliminar_procesador, name="eliminar_procesador"),
    path('procesador/<int:id>/editar/', views.editar_procesador, name="editar_procesador"),

   # urls necesarias para mostrar todo lo referente a los sistemas que se agregan, actualizan, editar y el listado de las misma 
    path('sistemaoperativo/', views.sistemaoperativo, name="sistemaoperativo"),
    path('sistemaoperativolista/', views.sistemaoperativolista, name="sistemaoperativolista"),
    path('guardar-sistemaoperativo/', views.guardar_sistemaoperativo, name="guardar_sistemaoperativo"),
    path('guardar-sistemaoperativo/<int:id>/', views.guardar_sistemaoperativo, name="actualizar_sistemaoperativo"),
    path('sistemaoperativo/<int:id>/eliminar/', views.eliminar_sistemaoperativo, name="eliminar_sistemaoperativo"),
    path('sistemaoperativo/<int:id>/editar/', views.editar_sistemaoperativo, name="editar_sistemaoperativo"),

   # urls necesarias para mostrar todo lo referente a los equipos que se agregan, actualizan, editar y el listado de las misma 
    path('equipo/', views.equipo, name="equipo"),
    path('reportetraslado/', views.reportetraslado, name="reportetraslado"),   # muestra lo reportes relacionados al equipo
    path('reportediagnostico/', views.reportediagnostico, name="reportediagnostico"),
    path('equipolista/', views.equipolista, name="equipolista"),
    path('guardar-equipo/', views.guardar_equipo, name="guardar_equipo"),
    path('guardar-equipo/<int:id>/', views.guardar_equipo, name="actualizar_equipo"),
    path('equipo/<int:id>/eliminar/', views.eliminar_equipo, name="eliminar_equipo"),
    path('equipo/<int:id>/editar/', views.editar_equipo, name="editar_equipo"),

   # urls necesarias para mostrar todo lo referente a las oficinas que se agregan, actualizan, editar y el listado de las misma 
    path('reporte/', views.reporte, name="reporte"),   # url que muestra el reporte de mantenimiento preventivo 
    path('mantenimiento/', views.mantenimiento, name="mantenimiento"),
    path('mantenimientolista/', views.mantenimientolista, name="mantenimientolista"),
    path('guardar-mantenimientopreventivo/', views.guardar_mantenimientopreventivo, name="guardar_mantenimientopreventivo"),
    path('guardar-mantenimientopreventivo/<int:id>/', views.guardar_mantenimientopreventivo, name="actualizar_mantenimientopreventivo"),
    path('mantenimientopreventivo/<int:id>/eliminar/', views.eliminar_mantenimientopreventivo, name="eliminar_mantenimientopreventivo"),
    path('mantenimientopreventivo/<int:id>/editar/', views.editar_mantenimientopreventivo, name="editar_mantenimientopreventivo"),

   # urls necesarias para mostrar todo lo referente a los airedatacenter  que se agregan, actualizan, editar y el listado de las misma 
    path('airedatacenter/', views.airedatacenter, name="airedatacenter"),
    path('airedatacenterlista/', views.airedatacenterlista, name="airedatacenterlista"),
    path('guardar-airedatacenter/', views.guardar_airedatacenter, name="guardar_airedatacenter"),
    path('guardar-airedatacenter/<int:id>/', views.guardar_airedatacenter, name="actualizar_airedatacenter"),
    path('airedatacenter/<int:id>/eliminar/', views.eliminar_airedatacenter, name="eliminar_airedatacenter"),
    path('airedatacenter/<int:id>/editar/', views.editar_airedatacenter, name="editar_airedatacenter"),

   # urls necesarias para mostrar todo lo referente a los protocolos que se agregan, actualizan, editar y el listado de las misma 
    path('protocolo/', views.protocolo, name="protocolo"),
    path('reporteprotocolo/', views.reporteprotocolo, name="reporteprotocolo"),
    path('protocololista/', views.protocololista, name="protocololista"),
    path('guardar-protocolo/', views.guardar_protocolo, name="guardar_protocolo"),
    path('guardar-protocolo/<int:id>/', views.guardar_protocolo, name="actualizar_protocolo"),
    path('protocolo/<int:id>/eliminar/', views.eliminar_protocolo, name="eliminar_protocolo"),
    path('protocolo/<int:id>/editar/', views.editar_protocolo, name="editar_protocolo"),

   # urls necesarias para mostrar todo lo referente a los detalles aire que se agregan, actualizan, editar y el listado de las misma 
    path('detalleaire/', views.detalleaire, name="detalleaire"),
    path('detalleairelista/', views.detalleairelista, name="detalleairelista"),
    path('guardar-detalleaire/', views.guardar_detalleaire, name="guardar_detalleaire"),
    path('guardar-detalleaire/<int:id>/', views.guardar_detalleaire, name="actualizar_detalleaire"),
    path('detalleaire/<int:id>/eliminar/', views.eliminar_detalleaire, name="eliminar_detalleaire"),
    path('detalleaire/<int:id>/editar/', views.editar_detalleaire, name="editar_detalleaire"),

   # urls necesarias para mostrar todo lo referente a los ups que se agregan, actualizan, editar y el listado de las misma 
    path('ups/', views.ups, name="ups"),
    path('upslista/', views.upslista, name="upslista"),
    path('guardar-ups/', views.guardar_ups, name="guardar_ups"),
    path('guardar-ups/<int:id>/', views.guardar_ups, name="actualizar_ups"),
    path('ups/<int:id>/eliminar/', views.eliminar_ups, name="eliminar_ups"),
    path('ups/<int:id>/editar/', views.editar_ups, name="editar_ups"),

   # urls necesarias para mostrar todo lo referente a los detalles lectura ups que se agregan, actualizan, editar y el listado de las misma 
    path('detallelectups/', views.detallelectups, name="detallelectups"),
    path('detallelectupslista/', views.detallelectupslista, name="detallelectupslista"),
    path('guardar-detallelectups/', views.guardar_detallelectups, name="guardar_detallelectups"),
    path('guardar-detallelectups/<int:id>/', views.guardar_detallelectups, name="actualizar_detallelectups"),
    path('detallelectups/<int:id>/eliminar/', views.eliminar_detallelectups, name="eliminar_detallelectups"),
    path('detallelectups/<int:id>/editar/', views.editar_detallelectups, name="editar_detallelectups"),

   # urls necesarias para mostrar todo lo referente a los ats que se agregan, actualizan, editar y el listado de las misma 
    path('ats/', views.ats, name="ats"),
    path('atslista/', views.atslista, name="atslista"),
    path('guardar-detalleats/', views.guardar_detalleats, name="guardar_detalleats"),
    path('guardar-detalleats/<int:id>/', views.guardar_detalleats, name="actualizar_detalleats"),
    path('detalleats/<int:id>/eliminar/', views.eliminar_detalleats, name="eliminar_detalleats"),
    path('detalleats/<int:id>/editar/', views.editar_detalleats, name="editar_detalleats"),

   # urls necesarias para mostrar todo lo referente a los detalles ats que se agregan, actualizan, editar y el listado de las misma 
    path('detalleats/', views.detalleats, name="detalleats"),
    path('detalleatslista/', views.detalleatslista, name="detalleatslista"),
    path('guardar-ats/', views.guardar_ats, name="guardar_ats"),
    path('guardar-ats/<int:id>/', views.guardar_ats, name="actualizar_ats"),
    path('ats/<int:id>/eliminar/', views.eliminar_ats, name="eliminar_ats"),
    path('ats/<int:id>/editar/', views.editar_ats, name="editar_ats"),

   # urls necesarias para mostrar todo lo referente a las alarmas sistemas que se agregan, actualizan, editar y el listado de las misma 
    path('alarmasistemas/', views.alarmasistemas, name="alarmasistemas"),
    path('alarmasistemaslista/', views.alarmasistemaslista, name="alarmasistemaslista"),
    path('guardar-alarmasistemas/', views.guardar_alarmasistemas, name="guardar_alarmasistemas"),
    path('guardar-alarmasistemas/<int:id>/', views.guardar_alarmasistemas, name="actualizar_alarmasistemas"),
    path('alarmasistemas/<int:id>/eliminar/', views.eliminar_alarmasistemas, name="eliminar_alarmasistemas"),
    path('alarmasistemas/<int:id>/editar/', views.editar_alarmasistemas, name="editar_alarmasistemas"),
] 
