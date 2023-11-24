from rest_framework import generics

from .models import User
from .serializers import UserSerializer
from .tasks import send_welcome_email


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post']

    def perform_create(self, serializer):
        """ Создание нового пользователя и вызов задачи из Celery """
        user = serializer.save()
        send_welcome_email.apply_async(args=[user.id], countdown=10)

    def get(self, request, *args, **kwargs):
        """ Получение списка всех пользователей """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Создание нового пользователя """
        return self.create(request, *args, **kwargs)
