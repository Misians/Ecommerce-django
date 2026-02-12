from rest_framework import generics, permissions
from .serializers import UserSerializer
from .models import User

# View para Registro de Cliente (aberta a todos)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]