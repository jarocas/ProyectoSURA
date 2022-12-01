from urllib import request
from django.shortcuts import render
from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formulariopacientes import FormularioPacientes
from web.models import Medicos
from web.models import Pacientes


# Create your views here.
#render (renderizar) es pintar
def Home(request):
    return render(request,'index.html')

def consultoriomedico(request):
    medicosConsultados = Medicos.objects.all()

    datosMedicos = {
        'medicos': medicosConsultados
    }
    return render(request, 'consultoriomedico.html', datosMedicos)

def consultarpaciente(request):
    pacientesConsultados = Pacientes.objects.all()

    datosPacientes = {
        'pacientes': pacientesConsultados
    }
    return render(request, 'consultarpaciente.html', datosPacientes)

def VistaMedicos (request):
    #creamos una variable para controlar la ejecusion de la alerta
    lanzandoAlerta = False

    #Debo utilizar la clase 'formularioMedico'
    # creamos entonces un objeto
    formulario=FormularioMedico()
    diccionario={
        "formulario":formulario,
        "bandera": lanzandoAlerta
    }
    #activar desde python la recepcion de datos
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos
            datos=datosRecibidos.cleaned_data
            medicoNuevo=Medicos(
                nombres=datos["Nombres"],
                apellidos=datos["Apellidos"],
                cedula=datos["Cedula"],
                tarjeta=datos["Tarjeta_Profesional"],
                especialidad=datos["Especialidad"],
                jornada=datos["Jornada"],
                contacto=datos["Contacto"],
                sede=datos["Sede"]
            )
            medicoNuevo.save()
            diccionario["bandera"] = True

    return render(request,'registrosmedicos.html',diccionario)

def vistaPacientes (request):
    lanzandoAlerta = False
    #Debo utilizar la clase 'formularioMedico'
    # creamos entonces un objeto
    formulario=FormularioPacientes()
    diccionario={
        "formulario":formulario,
        "bandera": lanzandoAlerta
    }
    #activar desde python la recepcion de datos
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioPacientes(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos
            datos=datosRecibidos.cleaned_data
            pacienteNuevo=Pacientes(
                nombres=datos["Nombres"],
                apellidos=datos["Apellidos"],
                cedula=datos["Cedula"],
                contacto=datos["Contacto"],
                correo=datos["Correo_electrónico"],
                afiliacion=datos["Tipo_de_afiliacion"],
                grupo=datos["Grupo"],
                copago=datos["Copago"]
            )
            pacienteNuevo.save()
            diccionario["bandera"] = True

    return render(request,'registropacientes.html',diccionario)

