from rest_framework import serializers
from .models import Post, Comment, Category



class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.ReadOnlyField(source='post.title')


    class Meta:
        model = Comment
        fields = ['id','comment', 'owner','post']

class CategoryPostSerializser(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True) 
    categories = CategoryPostSerializser(many=True, read_only=True)   
    categoryId = serializers.PrimaryKeyRelatedField(many=True, write_only=True,queryset=Category.objects.all(), source='categories')

    class Meta:
        model = Post
        fields = ['id','title', 'body', 'owner', 'comments', 'categories','categoryId']


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id','name','description','owner','posts']