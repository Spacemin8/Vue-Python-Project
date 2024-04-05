from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
class Token(models.Model):
    accesstoken = models.CharField(max_length=255)
    refreshtoken = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    
class verify(models.Model):
    email = models.EmailField(max_length=100, null=True)
    verification_code = models.CharField(max_length=10)
    expire_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.email
