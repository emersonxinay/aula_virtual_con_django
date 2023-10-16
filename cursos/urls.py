from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('registrar/curso/', views.registrar_curso, name='registrar_curso'),
    path('registrar/leccion/', views.registrar_leccion, name='registrar_leccion'),
    path('registrar/evaluacion/', views.registrar_evaluacion, name='registrar_evaluacion'),
]
