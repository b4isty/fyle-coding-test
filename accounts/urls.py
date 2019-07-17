from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import RegisterViewAPI
app_name = 'accounts'

urlpatterns = [
    path('auth-token/', obtain_jwt_token, name='login'),
    path('refresh-token/', refresh_jwt_token, name='refresh-token'),
    path('verify-token/', verify_jwt_token, name='verify-token'),
    path('signup/', RegisterViewAPI.as_view(), name='signup'),
]




