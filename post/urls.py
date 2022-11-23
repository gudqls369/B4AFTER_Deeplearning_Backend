from django.urls import path
from post.views import PostView, PostDetailView

urlpatterns = [
    path('', PostView.as_view(), name="main_view"),
    path('<int:post_id>/', PostDetailView.as_view(), name="post_detail_view"),
]