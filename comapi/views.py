from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

from comapi.serializers import UserSerializer, BoardSerializer, PostSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from comapi.models import Board, BoardPost



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = ()


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class BoardPost(generics.CreateAPIView):

    queryset = BoardPost.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user, parent_board=self.request.body.board)