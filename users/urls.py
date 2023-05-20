from django.urls import path, include
from rest_framework import routers
from .views import CreateTokenView,UserView


router = routers.DefaultRouter()
router.register('', UserView, 'users')


urlpatterns = [
    path('',include(router.urls) ),
    #Endpoints de usuarios: Metodos Post y Get no requieren autenticación
    #Metodos Put, Patch y Delete requieren autenticación y ser propietario del perfil para realizar estas acciones
    path('auth/login/', CreateTokenView.as_view()),
    #Login de usuario genera un token de autenticación
    #El usuario debe estar previamente registrado y deberá ingresar su usuario y contraseña para autenticarse
]