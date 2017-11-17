from rest_framework import viewsets
from rest_framework.response import Response

from ComBoard.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer