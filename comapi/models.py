# models.py

# DATABASE Models

from django.contrib.gis.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.contrib.auth import get_user_model


#For Board/BoardPost on_delete. Deleted Users will not affect existing Boards.
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Board(models.Model):
    public_viewable = models.BooleanField(default=False)
    viewable_radius = models.IntegerField()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    location = models.GeometryField()
    creator = models.ForeignKey('auth.User', on_delete=models.SET(get_sentinel_user))


class BoardPost(models.Model):
    parent_board = models.ForeignKey(Board, on_delete=models.SET(get_sentinel_user))
    post_title = models.CharField(max_length=200)
    post_body = models.CharField(max_length=4000)

class BoardUser(models.Model):
    token = models.CharField(max_length=1000)
    legacy_boards = models.ManyToManyField(Board)
    user = models.OneToOneField(User, on_delete=models.CASCADE)