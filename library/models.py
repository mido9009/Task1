from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# Author:
# 	name
# 	birth_date
# 	biography
# Book:
# 	title
# 	autor
# 	publication_date
# 	price
# Review:
#     	book
#     	reviewer_name
#     	content
#     	rating(1:5)
# ----------------------------
# ToDo:
#     	- github repo with project
#    	- design models
#     	- Generate CRUD for Books


class Author(models.Model):
    name = models.CharField(max_length=10)
    birth_date = models.DateField()
    biography = models.TextField(max_length=1000)


class Book(models.Model):
    title = models.CharField(max_length=10)
    autor = models.ForeignKey(Author, related_name="Book_author", on_delete=models.CASCADE)
    publication_date = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()
    review = models.ForeignKey("Review", related_name="Book_review", on_delete=models.SET_NULL,null=True)

class Review(models.Model):
    reviewer_name = models.CharField(max_length=20)
    content = models.TextField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=1)