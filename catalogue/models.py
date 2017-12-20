from django.db import models

class Book(models.Model):
    filepath = models.CharField(max_length=200)
    filename = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    seen = models.DateTimeField()
