from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique = True)
    phoneNumber = models.CharField(max_length=25)
    username = models.CharField(max_length=255)
    # is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()


# class Notepad(models.Model):
#     name= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     body = models.TextField()

# class Student(models.Model):
#     name=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     department = models.CharField(max_length=100)
#     level = models.IntegerField()
#     school = models.CharField(max_length=100)

#     def __str__(self):
#         return self.department
