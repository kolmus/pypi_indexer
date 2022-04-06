from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    guid = models.CharField(max_length=256)
    description = models.TextField(max_length=256, null=True)
    author = models.CharField(max_length=256, null=True)
    pub_date = models.DateTimeField()
