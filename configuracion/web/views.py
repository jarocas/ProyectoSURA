from urllib import request
from django.shortcuts import render
from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formulariopacientes import FormularioPacientes

# Create your views here.
#render (renderizar) es pintar
def Home(request):
    return render(request,'index.html')

def Medicos (request):
    #Debo utilizar la clase 'formularioMedico'
    # creamos entonces un objeto
    formulario=FormularioMedico()
    diccionario={
        "formulario":formulario
    }
    #activar desde python la recepcion de datos
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos
            datos=datosRecibidos.cleaned_data
            print(datos)

    return render(request,'registrosmedicos.html',diccionario)

def Pacientes (request):
    #Debo utilizar la clase 'formularioMedico'
    # creamos entonces un objeto
    formulario=FormularioPacientes()
    diccionario={
        "formulario":formulario
    }
    #activar desde python la recepcion de datos
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioPacientes(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos
            datos=datosRecibidos.cleaned_data
            print(datos)

    return render(request,'registropacientes.html',diccionario)

