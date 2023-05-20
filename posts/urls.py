from django.urls import path, include
from rest_framework import routers
from .views import PostView


router = routers.DefaultRouter()
router.register('posts', PostView, 'posts')


urlpatterns = [
    path('',include(router.urls) ),
    #Endpoints de usuarios: El metodo Get no requieren autenticación
    #Metodos Post, Put, Patch y Delete requieren autenticación y permisos de administrador para realizar estas acciones
]