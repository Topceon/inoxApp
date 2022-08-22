from django.db import models


class Storage(models.Model):
    name = models.CharField(max_length=100)
