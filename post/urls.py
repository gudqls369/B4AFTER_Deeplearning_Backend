from django.urls import path
from post.views import PostView, PostDetailView, CommentView, CommentDetailView

urlpatterns = [
    path('', PostView.as_view(), name="main_view"),
    path('<int:post_id>/', PostDetailView.as_view(), name="post_detail_view"),
    path('<int:post_id>/comment/', CommentView.as_view(), name="comment_view"),
    path('<int:post_id>/comment/<int:comment_id>/', CommentDetailView.as_view(), name="comment_detail_view"),
]
