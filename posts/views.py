from rest_framework import viewsets, authentication, permissions
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_permissions(self):

        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
    
        return super(PostView,self).get_permissions()
    
    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)
