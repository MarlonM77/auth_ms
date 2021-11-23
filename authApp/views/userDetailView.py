from authApp.models.user                import User
from rest_framework                     import status
from rest_framework.response            import Response
from django.db.models.query             import QuerySet
from authApp.serializers.userSerializer import UserSerializer
from rest_framework                     import generics, serializers


class UserDetailView(generics.RetrieveAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class UserUpdateView(generics.UpdateAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        return super().update(self, request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)




