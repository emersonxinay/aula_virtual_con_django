from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Curso(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    def __str__(self):
        return self.titulo

class Leccion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    def __str__(self):
        return self.titulo

class Evaluacion(models.Model):
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=255)
    opciones = models.JSONField()
    respuesta_correcta = models.CharField(max_length=255)
    def __str__(self):
        return self.pregunta
    
