from faulthandler import cancel_dump_traceback_later
from django import forms
class FormularioMedico(forms.Form):

    ESPECIALIDADES = (
        (1, 'Cardiología'),
        (2, 'Medicina Interna'),
        (3, 'Medico General'),
        (4, 'Ortopedia'),
        (5, 'Pediatria')
    )
    JORNADAS = (
        (1, '6-14'),
        (2, '14-22'),
        (3, '22-6')
    )
    SEDES = (
        (1, 'Almacentro'),
        (2, 'Punto Clave'),
        (3, 'Los Molinos')
    )

    nombre = forms.CharField() 
    apellidos = forms.CharField() 
    cedula = forms.CharField() 
    tarjetaProfesional = forms.CharField() 
    especialidad = forms.ChoiceField()
    jornada = forms.ChoiceField()
    contacto = forms.CharField() 
    sede = forms.ChoiceField()