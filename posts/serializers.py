from rest_framework import serializers
from .models import Post, Comment, Category



class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.ReadOnlyField(source='post.title')


    class Meta:
        model = Comment
        fields = ['id','comment', 'owner','post']

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True) 
    categories = serializers.StringRelatedField(many=True)   

    class Meta:
        model = Post
        fields = ['id','title', 'body', 'owner', 'comments', 'categories']


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id','name','description','owner','posts']