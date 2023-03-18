from django.urls import path
from .api.user import UserInfoAPIView

urlpatterns = [
    path('user/info', UserInfoAPIView.as_view(), name='user_info'),
]
