from rest_framework import viewsets, authentication, permissions
from .models import Post, Comment, Category
from .serializers import PostSerializer,CommentSerializer, CategorySerializer
from .permisions import IsOwnerOrReadOnly

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

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_permissions(self):

        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        elif self.request.method == 'POST':
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

        return super(CommentView,self).get_permissions()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super(CategoryView,self).get_permissions()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
