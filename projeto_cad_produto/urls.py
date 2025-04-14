from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    #usuarios.com
    #view é a função do que vai fazer quando chegar na path (rota)
    path('',views.home, name='home'),

    #usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios'),

    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),

    path('usuarios/excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
]
