from rest_framework import serializers
from post.models import Post, Image, Comment

class CommentSerializer(serializers.modelserializer):
    class meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.modelserializer):
    class meta:
        model = Comment
        fields = ('content',)

class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('image', 'content')
