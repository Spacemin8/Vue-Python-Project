from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)