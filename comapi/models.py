# models.py

# DATABASE Models

from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# For Board/BoardPost on_delete. Deleted Users will not affect existing Boards.
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


# Board model 
class Board(models.Model):
    public_viewable = models.BooleanField(default=False)
    viewable_radius = models.IntegerField()
    board_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    location = models.GeometryField()
    creator = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))


# Board User Model
# note: BoardUser is accociated with a User (from models.USer)
class BoardUser(models.Model):
    legacy_boards = models.ManyToManyField(Board)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# Board Post Model
# posts have parents and creators as Foreign Keys
class BoardPost(models.Model):
    parent_board = models.ForeignKey(Board, related_name='posts', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                     default="", blank=False)
    post_title = models.CharField(max_length=200)
    post_body = models.CharField(max_length=4000)
    pub_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
