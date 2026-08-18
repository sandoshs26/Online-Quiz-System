from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):

    roles = (
            ("ADMIN","Admin"),
            ("TEACHER","Teacher"),
            ("STUDENT","Student"),
        )
    
    phone_number = models.CharField(max_length=16,blank=True)
    role = models.CharField(max_length=10, default="STUDENT", choices=roles)

    def __str__(self):
        return self.username

    