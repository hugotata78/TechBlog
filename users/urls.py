from django.urls import path, include
from rest_framework import routers
from .views import UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

router = routers.DefaultRouter()
router.register('', UserView, 'users')


urlpatterns = [
    path('',include(router.urls) ),
    #Endpoints de usuarios: Metodos Post y Get no requieren autenticación
    #Metodos Put, Patch y Delete requieren autenticación y ser propietario del perfil para realizar estas acciones
    path('auth/token/', TokenObtainPairView.as_view(), name='token'),
    path('auth/token_refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='logout'),
    #Login de usuario genera un token de autenticación
    #El usuario debe estar previamente registrado y deberá ingresar su usuario y contraseña para autenticarse
]