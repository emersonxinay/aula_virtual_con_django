from django import forms
from .models import Usuario, Curso, Leccion, Evaluacion

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo_electronico', 'contrasena']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descripcion', 'duracion']

class LeccionForm(forms.ModelForm):
    class Meta:
        model = Leccion
        fields = ['curso', 'titulo', 'contenido']

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['leccion', 'pregunta', 'opciones', 'respuesta_correcta']
