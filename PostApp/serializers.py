from rest_framework import serializers
from .models import Post,Category
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Post
        fields = ('title','desk','slug','user_id','cat')
        
class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    
    class Meta:
        model = Post
        fields = ('name','slug')
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('__all__')
