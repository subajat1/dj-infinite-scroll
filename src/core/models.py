# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Journal(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, related_name='journal_author', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    publish_date = models.DateTimeField(auto_now_add=False)
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
