from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_path = models.CharField(max_length=100, null=True, blank=True)

class ExternalLink(models.Model):
    name = models.CharField(max_length=50)
    descriptiion = models.TextField()
    url = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100, null=True, blank=True)
