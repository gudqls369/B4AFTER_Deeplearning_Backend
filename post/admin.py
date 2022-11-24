from django.contrib import admin
from post.models import Post, Image, Comment, ImageModel

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(ImageModel)