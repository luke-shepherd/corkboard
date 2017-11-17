#models.py

#DATABASE Models 

from django.contrib.gis.db import models

class Board(models.Model):
	public_viewable = models.BooleanField(default=False)
	viewable_radius = models.IntegerField()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    location = models.GeometryField()
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class BoardPost(models.Model):
	parent_board = models.ForeignKey(Board, on_delete=models.CASCADE)
	post_title = models.CharField(max_length=200)
	post_body = models.CharField(max_length=4000)



