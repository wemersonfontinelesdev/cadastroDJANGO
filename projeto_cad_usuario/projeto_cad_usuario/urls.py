
#from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views #IMPORTEI ISSO
#unica parte que importa
#rota, view responsável, nome de referencia
urlpatterns = [
  #  path('') - fecebook.com,
  #  path('wemerson')fecebook.com/wemerson,
    path('',views.home, name='home'),
    path('usuarios/',views.usuarios, name='listagem_usuarios')
]
