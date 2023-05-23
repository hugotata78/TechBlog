from rest_framework import viewsets, authentication, permissions, generics, decorators
from rest_framework.response import Response
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

class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, post_id=self.kwargs['pk'])

class RetrieveUpdateDestroyCommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_permissions(self):

        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

        return super(RetrieveUpdateDestroyCommentView,self).get_permissions()
    

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
