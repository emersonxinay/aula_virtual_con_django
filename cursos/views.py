from django.shortcuts import render
from .forms import UsuarioForm, CursoForm, LeccionForm, EvaluacionForm
def home(request):
    return render(request, 'home.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render(request, 'cursos/registrar_usuario.html', {'form': form})

def registrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoForm()
    return render(request, 'cursos/registrar_curso.html', {'form': form})

def registrar_leccion(request):
    if request.method == 'POST':
        form = LeccionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LeccionForm()
    return render(request, 'cursos/registrar_leccion.html', {'form': form})

def registrar_evaluacion(request):
    if request.method == 'POST':
        form = EvaluacionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EvaluacionForm()
    return render(request, 'cursos/registrar_evaluacion.html', {'form': form})
