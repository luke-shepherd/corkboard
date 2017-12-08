from rest_framework import serializers
from django.contrib.auth.models import User
from comapi.models import Board, BoardPost, BoardUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')



class BoardUserSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    legacy_boards = serializers.PrimaryKeyRelatedField(many=True, queryset=Board.objects.all())

    class Meta:
        model = BoardUser
        fields = ('user', 'legacy_boards')
        


class BoardSerializer(serializers.HyperlinkedModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=BoardPost.objects.all())

    class Meta:
        model = Board
        fields = ('public_viewable', 'viewable_radius', 'board_name', 'pub_date', 
                  'edit_date', 'location', 'creator', 'posts')


class PostSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    #parent_board = serializers.HyperlinkedRelatedField(read_only=True, view_name='BoardPost')

    class Meta:
        model = BoardPost
        fields = ('creator', 'post_title', 'post_body', 'pub_date',
                  'edit_date')
