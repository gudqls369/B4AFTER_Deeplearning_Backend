from django.urls import path
from rest_framework_simplejwt.views import ( #simplejwt 기본 기능 import, simplejwt 공식문서 참고
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserView
 
urlpatterns = [
    path('signup/', UserView.as_view(), name='user_view'), #회원가입 URL
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #simplejwt 기본 기능
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #simplejwt 기본 기능
]