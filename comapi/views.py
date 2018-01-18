from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from comapi.serializers import UserSerializer, BoardDetailSerializer, BoardListSerializer, PostSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from comapi.models import Board, BoardPost
from rest_framework import status, permissions


# Accociated with /users/
# lists Users and provides POST for user creation. 
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Accociated with /users/[id]
# sends single user view 
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = ()

# Accociated with /boards/
# lists Boards and provides POST for board creation.
class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardListSerializer

    # modified to link created boards with users
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

# Accociated with /boards/[id]
# sends single board view 
class BoardDetail(generics.ListAPIView):
    queryset = ''
    serializer_class = BoardDetailSerializer
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):

        # searches boards for specified id
        queryset = Board.objects.filter(pk=self.kwargs['pk'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# Accociated with /board_posts/[id]
# sends single board post view (using id)
# provides POST for board post creation
class BoardPostList(generics.ListCreateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer
    queryset = '' #need to declare queryset even though it's declared and filtered in list method

    def perform_create(self, serializer):

        b = Board.objects.get(pk=self.kwargs['pk'])
        serializer.save(creator=self.request.user, parent_board=b)


    def list(self, request, *args, **kwargs):

        # search posts for specified board id
        queryset = BoardPost.objects.filter(parent_board=self.kwargs['pk'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)








        