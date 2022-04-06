from django.db import models


# Create your models here.
class Item (models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    guid = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    author = models.CharField(max_length=256)
    pub_date = models.DateTimeField()
    