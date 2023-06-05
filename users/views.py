from rest_framework import viewsets, permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from .serializers import AuthTokenSerializer, UserSerializer, MyTokenObteinPairSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

"""
Conjunto de vistas de Usuarios:
los metodos GET y POST no requieren autenticación ni permisos
los metodos PUT, PATCH y DELETE requieren autenticación y y el usuario debe tener permisos
de propietario para poder realizar estas acciones
"""

class UserView(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    

    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'POST':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
        return super(UserView,self).get_permissions()

"""
Vista de Login de usuario el cual genera un token de autenticación
el usuario primero deberá registrarse y luego para loguearse
deberá ingresar su nombre de usuario y contraseña para autenticarse
"""
class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObteinPairSerializer
