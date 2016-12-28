from django.db import models

# Create your models here.
class Hackening(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    content = models.TextField()
