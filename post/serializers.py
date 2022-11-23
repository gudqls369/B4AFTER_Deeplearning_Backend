from rest_framework import serializers
from post.models import Post, Image, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)

class ImageSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username
    class Meta:
        model = Image
        fields = '__all__'

class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('before_image', 'after_image')

class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    image = ImageSerializer()

    def get_user(self, obj):
        return obj.user.username

    def get_image(self, obj):
        return obj.image

    def get_comments(self, obj):
        return obj.comments

    class Meta:
        model = Post
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    image = ImageSerializer()

    def get_user(self, obj):
        return obj.user.username
        
    class Meta:
        model = Post
        fields = ('user','image', 'content')

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('content',)