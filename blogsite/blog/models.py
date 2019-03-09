# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

@python_2_unicode_compatible
class Story(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	text = models.TextField()
	published_date = models.DateField()


	def __str__(self):
		return self.title

	# @property
	# def json_equivalent(self):
	# 	dictionary = {}
	# 	for field in self._meta.fields:
	# 		dictionary[field.name] = self.__getattribute__(field.name)
	# 	return dictionary


# @python_2_unicode_compatible
class StoryMetaData(models.Model):
	view_count = models.IntegerField(default=0)
	likes_count = models.IntegerField(default=0)
	last_viewed = models.DateField()
	story = models.ForeignKey(Story)

	def __str__(self):
		return self.story.title + ": Likes :" + str(self.likes_count) 