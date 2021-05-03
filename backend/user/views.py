from django.contrib.auth.models import User
from rest_framework import generics
from api import permissions
from user.serializers import UserSerializer
from rest_framework import permissions as perm


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (perm.IsAuthenticated, perm.IsAdminUser)
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (perm.IsAuthenticated, permissions.UserPermission or perm.IsAdminUser, )
