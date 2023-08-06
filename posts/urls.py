from django.urls import path, include
from rest_framework import routers
from .views import PostView,CategoryView,RetrieveUpdateDestroyCommentView, CreateCommentView


router = routers.DefaultRouter()
router.register('posts', PostView, 'posts')
router.register('categories', CategoryView,'categories')
comment_creation = PostView.as_view({
    'post': 'set_comment'
})



urlpatterns = [
    path('',include(router.urls) ),
    path('posts/<int:pk>/comment/',CreateCommentView.as_view()),
    path('comments/<int:pk>/', RetrieveUpdateDestroyCommentView.as_view())
    #Endpoints de Post: El metodo Get no requieren autenticación
    #Metodos Post, Put, Patch y Delete requieren autenticación y permisos de administrador para realizar estas acciones
    #Endpoints de Comments: El metodo Get no requieren autenticación
    #Metodos Post requiere que el usuario este autenticado para crear un comentario
    # Metodos Put, Patch y Delete requieren autenticación de usuario y permiso de propietario para realizar estas acciones
]