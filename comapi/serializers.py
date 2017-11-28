from rest_framework import serializers
from django.contrib.auth.models import User
from comapi.models import Board


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class BoardSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Board
        fields = ('public_viewable', 'viewable_radius', 'question_text', 'pub_date', 
                  'edit_date', 'location', 'creator')