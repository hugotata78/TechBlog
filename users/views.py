from rest_framework import viewsets, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer, MyTokenObteinPairSerializer, UserAuthenticateSerializer
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

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObteinPairSerializer

    def post(self, request, *args, **kwargs):

        username = request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(
            username = username,
            password = password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserAuthenticateSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Existoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

