from faulthandler import cancel_dump_traceback_later
from django import forms
class FormularioMedico(forms.Form):

    ESPECIALIDADES = (
        (0, "Selecciona una especialidad.."),
        (1, 'Cardiología'),
        (2, 'Medicina Interna'),
        (3, 'Medico General'),
        (4, 'Ortopedia'),
        (5, 'Pediatria')
    )
    JORNADAS = (
        (0, "Selecciona un Turno..."),
        (1, '6-14'),
        (2, '14-22'),
        (3, '22-6')
    )
    SEDES = (
        (0, "Selecciona una sede..."),
        (1, 'Almacentro'),
        (2, 'Punto Clave'),
        (3, 'Los Molinos')
    )

    Nombre = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=15
    ) 
    Apellidos = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=35
    ) 
    Cedula = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=10
    ) 
    Tarjeta_Profesional = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=20
    ) 
    especialidad = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=ESPECIALIDADES
    )
    Jornada = forms.ChoiceField(
         widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=JORNADAS
    )
    Contacto = forms.CharField(
         widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=20
    ) 
    Sede = forms.ChoiceField(
         widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=SEDES
    )