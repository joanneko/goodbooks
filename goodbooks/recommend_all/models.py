from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=100)
	author_first = models.CharField(max_length=20)
	author_last = models.CharField(max_length=20)
	user = models.CharField(max_length=20)

# need movie and music class 
