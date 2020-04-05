
from django.db import models
from django.contrib.auth.models import User

#creamos la tabla  marca
class Marca(models.Model):
    marca = models.CharField(max_length=60)

    def __str__(self):
        return self.marca
#creamos la tabla  modelo
class Modelo(models.Model):
    modelo= models.CharField(max_length=60)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE,null=True, blank=True)
 
    def __str__(self):
        return self.modelo
#creamos la tabla  estado
class Estado(models.Model):
    estado = models.CharField(max_length=60)

    def __str__(self):
        return self.estado
#creamos la tabla oficina
class Oficina(models.Model):
    codoficina= models.CharField(max_length=6)
    oficina = models.CharField(max_length=60)
  
 
    def __str__(self):
        return self.oficina

#creamos la tabla departamento 
class Departamento(models.Model):
    departamento = models.CharField(max_length=60)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.departamento
#creamos la tabla lugar reparaciones  
class LugarReparacion(models.Model):
    lugarreparacion = models.CharField(max_length=60)

    def __str__(self):
        return self.lugarreparacion
#creamos la tabla usuario  
class Usuario(models.Model):
    codusuario = models.CharField(max_length=60)
    nombreusuario = models.CharField(max_length=60)
    contrasena = models.CharField(max_length=25)
    correo = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)

#creamos la tabla auditoria  
class Auditoria(models.Model):
    descripcion = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50) 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.descripcion, self.fecha)
#creamos la tabla equipo  
class Equipo(models.Model):
    codequipo = models.CharField(max_length=15)
    nombreequipo= models.CharField(max_length=70)
    fechacompra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    observacion = models.CharField(max_length=100)
    diagnosticada = models.CharField(max_length=60)
    discoduro = models.CharField(max_length=60)
    servicetag = models.CharField(max_length=60)
    direccionip = models.CharField(max_length=60)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True, blank=True)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE,null=True, blank=True)
    lugarreparacion = models.ForeignKey(LugarReparacion, on_delete=models.CASCADE,null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE,null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.codequipo, self.usuario)
#creamos la tabla pocesador
class Procesador (models.Model):
    procesador = models.CharField(max_length=150)
    cpu = models.CharField(max_length=100)
    equipo =models.ForeignKey(Equipo, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.procesador
#creamos la tabla sistema operativo
class SistemaOperativo(models.Model):
    sistemaoperativo= models.CharField(max_length=100)
    equipo =models.ForeignKey(Equipo, on_delete=models.CASCADE,null=True, blank=True)
   
    def __str__(self):
        return self.sistemaoperativo
#creamos la tabla mantenimiento preventivo
class MantenimientoPreventivo(models.Model):
    fechamantenimiento = models.CharField(max_length=100)
    realizado =models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    oficina =models.ForeignKey(Oficina, on_delete=models.CASCADE,null=True, blank=True)
    usuario =models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.fechamantenimiento
#creamos la tabla airedatacenter
class AireDatacenter(models.Model):
    codaire= models.CharField(max_length=10)
    nombreaire =models.CharField(max_length=50)
    modeloaire =models.CharField(max_length=50)
    marcaaire =models.CharField(max_length=50)
    serieaire =models.CharField(max_length=50)
    nombrecondensadoraaire =models.CharField(max_length=50)
    modelocondensadoraaire =models.CharField(max_length=50)
    seriecondensadoraaire =models.CharField(max_length=50)

    def __str__(self):
        return self.codaire
#creamos la tabla protocolo
class Protocolo(models.Model):
    fechaprotocolo =models.CharField(max_length=17)
    historialeventos =models.CharField(max_length=20)
    temperaturadata=models.CharField(max_length=5)
    humedaddata =models.CharField(max_length=5)
    revisionequipos =models.CharField(max_length=200)
    observaciones =models.CharField(max_length=200)
    panelregulado =models.CharField(max_length=5)
    panelnoregulado =models.CharField(max_length=5)
    ventosasenposicion =models.CharField(max_length=5)
    boquillaaerea =models.CharField(max_length=5)
    boquillabajopiso =models.CharField(max_length=5)
    lucesprincipalesbuenestado =models.CharField(max_length=5)
    camarafuncionando=models.CharField(max_length=5)
    oaverde = models.CharField(max_length=5)
    ocverde=models.CharField(max_length=5)
    hora =models.CharField(max_length=8)
    lucessalida =models.CharField(max_length=5)
    usuario =models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.fechaprotocolo
#creamos la tabla detalle aire 
class DetalleAire(models.Model):
    aire =models.ForeignKey(AireDatacenter, on_delete=models.CASCADE,null=True, blank=True)
    protocolo =models.ForeignKey(Protocolo, on_delete=models.CASCADE,null=True, blank=True)
    alarmaaire =models.CharField(max_length=4)
    aireencendido =models.CharField(max_length=4)
    horaaire =models.CharField(max_length=8)
    temperaturaaire =models.CharField(max_length=15)
    humedadaire =models.CharField(max_length=15)

    def __str__(self):
        return self.temperaturaaire
#creamos la tabla ups
class Ups(models.Model):
    codups = models.CharField(max_length=10)
    nombreups =models.CharField(max_length=50)
    modeloups =models.CharField(max_length=50)
    marcaups =models.CharField(max_length=50)
    serieups =models.CharField(max_length=50)

    def __str__(self):
        return self.codups
#creamos la tabla detalle lectura ups
class DetalleLectUps(models.Model):
    ups =models.ForeignKey(Ups, on_delete=models.CASCADE,null=True, blank=True)
    protocolo =models.ForeignKey(Protocolo, on_delete=models.CASCADE,null=True, blank=True)
    alarmaups =models.CharField(max_length=4)
    bateriaups =models.CharField(max_length=4)
    cargaups =models.CharField(max_length=4)
    ventups =models.CharField(max_length=4)
    vsalups =models.CharField(max_length=4)
    hertzups =models.CharField(max_length=4)
    czasups =models.CharField(max_length=4)
    prhorasups =models.CharField(max_length=4)
    prminutosups =models.CharField(max_length=4)    

    def __str__(self):
        return self.cargaups
#creamos la tabla alarma sistemas 
class AlarmaSistemas(models.Model):
    alarmacontraincendio =models.CharField(max_length=4)
    alarmacontraincendiohabilitado =models.CharField(max_length=4)
    cilindroprincipallleno =models.CharField(max_length=4)
    cilindromanual =models.CharField(max_length=4)
    protocolo =models.ForeignKey(Protocolo, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.alarmacontraincendio
#creamos la tabla airedatacenter
class Ats(models.Model):
    codats = models.CharField(max_length=10)
    nombreats =models.CharField(max_length=50)
    modeloats =models.CharField(max_length=50)
    marcaats =models.CharField(max_length=50)
    serieats =models.CharField(max_length=50)

    def __str__(self):
        return self.codats
#creamos la tabla detalle ats
class DetalleAts(models.Model):
    ats =models.ForeignKey(Ats, on_delete=models.CASCADE,null=True, blank=True)
    protocolo =models.ForeignKey(Protocolo, on_delete=models.CASCADE,null=True, blank=True)
    lucesencendidasayb =models.CharField(max_length=4)
    preferencia = models.CharField(max_length=4)
    amps = models.CharField(max_length=4)


    def __str__(self):
        return self.preferencia