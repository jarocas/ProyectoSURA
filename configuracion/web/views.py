from urllib import request
from django.shortcuts import render
from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formulariopacientes import FormularioPacientes
from web.models import Medicos

# Create your views here.
#render (renderizar) es pintar
def Home(request):
    return render(request,'index.html')

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

def Pacientes (request):
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
                cedula=datos["Césdula"],
                contacto=datos["Contacto"],
                correo=datos["Correo_electrónico"],
                afiliacion=datos["Tipo_de_afiliación"],
                grupo=datos["Grupo"],
                copago=datos["Copago"]
            )
            pacienteNuevo.save()
            diccionario["bandera"] = True

    return render(request,'registropacientes.html',diccionario)

