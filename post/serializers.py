from rest_framework import serializers
from post.models import Post, Image, Comment


class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('image', 'content')
