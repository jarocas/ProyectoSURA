from faulthandler import cancel_dump_traceback_later
from django import forms
class FormularioPacientes(forms.Form):

    TIPOAFILIACION = (
        (0, 'Seleccionar Afiliación...'),
        (1, 'P. Excepción'),
        (2, 'E. Especial'),
        (3, 'C. Contributivo'),
        (4, 'S. Subsidiado'),
        (5, 'N. No Asegurado'),
        (6, 'I. Indeterminado/Pendiente')
    )
    GRUPO = (
        (0, 'Seleccionar el Grupo...'),
        (1, 'A'),
        (2, 'B'),
        (3, 'C')
    )
    COPAGO = (
        (0, 'Seleccionar el Copago...'),
        (1, 'Nivel A: $3.700'),
        (2, 'Nivel B: $14.700'),
        (3, 'Nivel C: $38.500')
    )

    
    Nombres = forms.CharField(
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
    Contacto = forms.CharField(
         widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=20
    ) 
    Correo_electrónico = forms.CharField(
         widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=20
    ) 
    Tipo_de_afiliacion = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=TIPOAFILIACION
    ) 
    Grupo = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=GRUPO
    )
    Copago = forms.ChoiceField(
         widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=COPAGO
    )
   
   