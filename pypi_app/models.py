from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=256)
    version = models.CharField(max_length=64)
    link = models.CharField(max_length=256)
    guid = models.CharField(max_length=256, null=True)
    description = models.TextField(max_length=256, null=True)
    author_name = models.CharField(max_length=256, null=True)
    author_email = models.CharField(max_length=256, null=True)
    pub_date = models.DateTimeField()
