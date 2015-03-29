import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	# Make object display in an easier to understand way
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		# How many days ago was it published?
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		was_published_recently.admin_order_field = 'pub_date'
		was_published_recently.boolean = True
		was_published_recently.short_description = 'Published Recently?'

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	# Make object easier to read
	def __str__(self):
		return self.choice_text