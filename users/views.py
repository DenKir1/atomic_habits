from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from users.models import User
from users.serializers import UserSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """ Пользователь """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]

    def create(self, request, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
