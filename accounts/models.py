from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):
    phone = models.CharField(max_length=45, null=True, blank=True)
    email = models.EmailField(max_length=45, null=True,blank=True)
    user_type = models.CharField(max_length=45, blank=True, null=True)
    
    def __str__(self):
            return f"{str(self.first_name)} - {self.user_type}"