from rest_framework import serializers
from django.contrib.auth.models import User
from comapi.models import Board, BoardPost, BoardUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')



class BoardUserSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = BoardUser
        fields = ('user', 'legacy_boards')
        


class BoardSerializer(serializers.HyperlinkedModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')
    posts = serializers.HyperlinkedIdentityField(view_name='posts')

    class Meta:
        model = Board
        fields = ('public_viewable', 'viewable_radius', 'question_text', 'pub_date', 
                  'edit_date', 'location', 'creator')


class PostSerializer(serializers.ModelSerializer):


    class Meta:
        model = BoardPost
        fields = ('parent_board', 'post_creator', 'post_title', 'post_body')