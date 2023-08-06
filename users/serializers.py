from rest_framework import serializers
from django.contrib.auth import get_user_model
from posts.serializers import PostSerializer,CategorySerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id','username', 'email', 'password','first_name','last_name', 'posts', 'categories']
        extra_kwargs = {
            'username':{'write_only':True},
            'email':{'write_only':True},
            'password':{'write_only':True}
            }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password',None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        
        return user
class UserAuthenticateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ['id','first_name','last_name']


class MyTokenObteinPairSerializer(TokenObtainPairSerializer):

    pass