from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *

#aqui en esta parte se crea cada uno de los formularios de cada tabla que se crearon en modelos 
#dandoles el tipo de datos y el espacio para poder ingresar el datoque se solicita 

class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

class MyAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

# creamos el formulario de oficina 
class OficinaForm(ModelForm):
    class Meta:
        model = Oficina#hacemos el llamdo del modelo 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['codoficina'].widget.attrs.update({'class': 'form-control'})
        self.fields['oficina'].widget.attrs.update({'class': 'form-control'})

# creamos el formulario de departamento 
class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento#hacemos el llamdo del modelo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['departamento'].widget.attrs.update({'class': 'form-control'})
        self.fields['oficina'].widget.attrs.update({'class': 'form-control'})

# creamos el formulario de marca
class  MarcaForm(ModelForm):
    class Meta:
        model = Marca#llamamos al modleo marca 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['marca'].widget.attrs.update({'class': 'form-control'})

# creamos el formulario de modelo
class  ModeloForm(ModelForm):
    class Meta:
        model = Modelo#llamamos al modelo Modelo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['modelo'].widget.attrs.update({'class': 'form-control'})
        self.fields['marca'].widget.attrs.update({'class': 'form-control'})
    
# creamos el formulario de estado
class  EstadoForm(ModelForm):
    class Meta:
        model = Estado#llamamos al modelo estado 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['estado'].widget.attrs.update({'class': 'form-control'})

# creamos el formulario de lugar reparacion 
class  LugarReparacionForm(ModelForm):
    class Meta:
        model = LugarReparacion#llamamaos al modelo lugar de reparacion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['lugarreparacion'].widget.attrs.update({'class': 'form-control'})

# creamos el formulario de usuario
class  UsuarioForm(ModelForm):
    class Meta:
        model = Usuario#llamamaos al modelo usuario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['codusuario'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreusuario'].widget.attrs.update({'class': 'form-control'})
        self.fields['contrasena'].widget.attrs.update({'class': 'form-control'})
        self.fields['correo'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido'].widget.attrs.update({'class': 'form-control'})


# creamos el formulario de auditoria
class  AuditoriaForm(ModelForm):
    class Meta:
        model = Auditoria
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha'].widget.attrs.update({'class': 'form-control'})
        self.fields['usuario'].widget.attrs.update({'class': 'form-control'})
    

# creamos el formulario procesador
class  ProcesadorForm(ModelForm):
    class Meta:
        model = Procesador#llamamos al modelo prosecador 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['procesador'].widget.attrs.update({'class': 'form-control'})
        self.fields['cpu'].widget.attrs.update({'class': 'form-control'})
        self.fields['equipo'].widget.attrs.update({'class': 'form-control'})
    

# creamos el formulario sistema operativo
class  SistemaOperativoForm(ModelForm):
    class Meta:
        model = SistemaOperativo#llamamos al modelo sistema operativo 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['sistemaoperativo'].widget.attrs.update({'class': 'form-control'})
        self.fields['equipo'].widget.attrs.update({'class': 'form-control'})

# creamos el formulario de equipo 
class  EquipoForm(ModelForm):
    class Meta:
        model = Equipo#llamamos al modelo Equipo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['codequipo'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreequipo'].widget.attrs.update({'class': 'form-control'})
        self.fields['fechacompra'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})
        self.fields['observacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['diagnosticada'].widget.attrs.update({'class': 'form-control'})
        self.fields['discoduro'].widget.attrs.update({'class': 'form-control'})
        self.fields['servicetag'].widget.attrs.update({'class': 'form-control'})
        self.fields['direccionip'].widget.attrs.update({'class': 'form-control'})
        self.fields['usuario'].widget.attrs.update({'class': 'form-control'})
        self.fields['oficina'].widget.attrs.update({'class': 'form-control'})
        self.fields['lugarreparacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})
        self.fields['modelo'].widget.attrs.update({'class': 'form-control'})

class  MantenimientoPreventivoForm(ModelForm):
    class Meta:
        model = MantenimientoPreventivo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fechamantenimiento'].widget.attrs.update({'class': 'form-control'})
        self.fields['realizado'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})
        self.fields['oficina'].widget.attrs.update({'class': 'form-control'})
        self.fields['usuario'].widget.attrs.update({'class': 'form-control'})
    

# creamos el formulario aire datacenter
class  AireDatacenterForm(ModelForm):
    class Meta:
        model = AireDatacenter#llamamos al modelo Aire datacebter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['codaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['modeloaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['marcaaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['serieaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombrecondensadoraaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['modelocondensadoraaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['seriecondensadoraaire'].widget.attrs.update({'class': 'form-control'})
    
# creamos el formulario de protocolo
class  ProtocoloForm(ModelForm):
    class Meta:
        model = Protocolo#llamamoa al modelo protocolo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fechaprotocolo'].widget.attrs.update({'class': 'form-control'})
        self.fields['historialeventos'].widget.attrs.update({'class': 'form-control'})
        self.fields['temperaturadata'].widget.attrs.update({'class': 'form-control'})
        self.fields['humedaddata'].widget.attrs.update({'class': 'form-control'})
        self.fields['revisionequipos'].widget.attrs.update({'class': 'form-control'})
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control'})
        self.fields['panelregulado'].widget.attrs.update({'class': 'form-control'})
        self.fields['panelnoregulado'].widget.attrs.update({'class': 'form-control'})
        self.fields['ventosasenposicion'].widget.attrs.update({'class': 'form-control'})
        self.fields['boquillaaerea'].widget.attrs.update({'class': 'form-control'})
        self.fields['boquillabajopiso'].widget.attrs.update({'class': 'form-control'})
        self.fields['lucesprincipalesbuenestado'].widget.attrs.update({'class': 'form-control'})
        self.fields['camarafuncionando'].widget.attrs.update({'class': 'form-control'})
        self.fields['oaverde'].widget.attrs.update({'class': 'form-control'})
        self.fields['ocverde'].widget.attrs.update({'class': 'form-control'})
        self.fields['hora'].widget.attrs.update({'class': 'form-control'})
        self.fields['lucessalida'].widget.attrs.update({'class': 'form-control'})
        self.fields['usuario'].widget.attrs.update({'class': 'form-control'})

# creamos el formulario detalle aire 
class  DetalleAireForm(ModelForm):
    class Meta:
        model = DetalleAire#llamamos al modelo detalle aire 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['aire'].widget.attrs.update({'class': 'form-control'})
        self.fields['protocolo'].widget.attrs.update({'class': 'form-control'})
        self.fields['alarmaaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['horaaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['temperaturaaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['humedadaire'].widget.attrs.update({'class': 'form-control'})


# creamos el formulario ups
class  UpsForm(ModelForm):
    class Meta:
        model = Ups#llamamos al modelo ups
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['codups'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreups'].widget.attrs.update({'class': 'form-control'})
        self.fields['modeloups'].widget.attrs.update({'class': 'form-control'})
        self.fields['marcaups'].widget.attrs.update({'class': 'form-control'})
        self.fields['serieups'].widget.attrs.update({'class': 'form-control'})

# creamos el formulario detalle lectura ups
class  DetalleLectUpsForm(ModelForm):
    class Meta:
        model = DetalleLectUps#llamamos al modelo detalle lectura uos
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['ups'].widget.attrs.update({'class': 'form-control'})
        self.fields['protocolo'].widget.attrs.update({'class': 'form-control'})
        self.fields['alarmaups'].widget.attrs.update({'class': 'form-control'})
        self.fields['bateriaups'].widget.attrs.update({'class': 'form-control'})
        self.fields['cargaups'].widget.attrs.update({'class': 'form-control'})
        self.fields['ventups'].widget.attrs.update({'class': 'form-control'})
        self.fields['vsalups'].widget.attrs.update({'class': 'form-control'})
        self.fields['hertzups'].widget.attrs.update({'class': 'form-control'})
        self.fields['czasups'].widget.attrs.update({'class': 'form-control'})
        self.fields['prhorasups'].widget.attrs.update({'class': 'form-control'})
        self.fields['prminutosups'].widget.attrs.update({'class': 'form-control'})

# creamos el formulario alarama sistemas 
class  AlarmaSistemasForm(ModelForm):
    class Meta:
        model = AlarmaSistemas#llamamos al modelo alarma sistemas 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['alarmacontraincendio'].widget.attrs.update({'class': 'form-control'})
        self.fields['alarmacontraincendiohabilitado'].widget.attrs.update({'class': 'form-control'})
        self.fields['cilindroprincipallleno'].widget.attrs.update({'class': 'form-control'})
        self.fields['cilindromanual'].widget.attrs.update({'class': 'form-control'})
        self.fields['protocolo'].widget.attrs.update({'class': 'form-control'})


# creamos el formulario ats
class AtsForm(ModelForm):
    class Meta:
        model = Ats#llamamos al modelo ats
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['codats'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreats'].widget.attrs.update({'class': 'form-control'})
        self.fields['modeloats'].widget.attrs.update({'class': 'form-control'})
        self.fields['marcaats'].widget.attrs.update({'class': 'form-control'})
        self.fields['serieats'].widget.attrs.update({'class': 'form-control'})


# creamos el formulario detalle ats 
class  DetalleAtsForm(ModelForm):
    class Meta:
        model = DetalleAts#llamamaos al modleo detalle ats 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['ats'].widget.attrs.update({'class': 'form-control'})
        self.fields['protocolo'].widget.attrs.update({'class': 'form-control'})
        self.fields['lucesencendidasayb'].widget.attrs.update({'class': 'form-control'})
        self.fields['preferencia'].widget.attrs.update({'class': 'form-control'})
        self.fields['amps'].widget.attrs.update({'class': 'form-control'})