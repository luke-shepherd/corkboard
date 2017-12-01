from rest_framework import viewsets
from rest_framework.response import Response

from comapi.serializers import UserSerializer, BoardSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from comapi.models import Board, BoardPost



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = ()


class BoardCreate(generics.GenericAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer