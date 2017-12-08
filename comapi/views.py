from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

from comapi.serializers import UserSerializer, BoardDetailSerializer, BoardListSerializer, PostSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from comapi.models import Board, BoardPost



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = ()


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardListSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class BoardDetail(generics.ListAPIView):
    queryset = ''
    serializer_class = BoardDetailSerializer
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):

        queryset = Board.objects.filter(pk=self.kwargs['pk'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BoardPostList(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    queryset = '' #need to declare queryset even though it's declared and filtered in list method

    def perform_create(self, serializer):
        b = Board.objects.get(pk=self.kwargs['pk'])
        serializer.save(creator=self.request.user, parent_board=b)

    def list(self, request, *args, **kwargs):

        queryset = BoardPost.objects.filter(parent_board=self.kwargs['pk'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)








        