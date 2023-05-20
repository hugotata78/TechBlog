from django.urls import path, include
from rest_framework import routers
from .views import PostView,CommentView


router = routers.DefaultRouter()
router.register('posts', PostView, 'posts')
router.register('comments', CommentView,'comments')


urlpatterns = [
    path('',include(router.urls) ),
    #Endpoints de Post: El metodo Get no requieren autenticación
    #Metodos Post, Put, Patch y Delete requieren autenticación y permisos de administrador para realizar estas acciones
    #Endpoints de Comments: El metodo Get no requieren autenticación
    #Metodos Post requiere que el usuario este autenticado para crear un comentario
    # Metodos Put, Patch y Delete requieren autenticación de usuario y permiso de propietario para realizar estas acciones
]