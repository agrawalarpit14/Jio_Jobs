from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
# Create your models here.

class Post(models.Model):
	gender = models.CharField(max_length=10)
	age = models.CharField(max_length=10)
	skills = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	priceperday = models.IntegerField(default=300)
	mobile = models.IntegerField(default=9837720000)
	date_posted = models.DateTimeField(auto_now_add= True)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs= {'pk': self.pk})

class Review(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	comment = models.CharField(max_length=100)
	user_name = models.CharField(max_length=100)
	# author = models.ForeignKey(User, on_delete = models.CASCADE)
	date_posted = models.DateTimeField(auto_now_add= True)
	
