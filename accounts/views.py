from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer

User = get_user_model()


class RegisterViewAPI(ListCreateAPIView):
    """
    API for signup
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
