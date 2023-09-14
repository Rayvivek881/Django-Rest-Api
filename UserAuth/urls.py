from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('jwtoken/get/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('jwtoken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('authtoken/get/', obtain_auth_token, name='obtain_auth_token'),
]
