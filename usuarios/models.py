from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    contact_details = models.TextField(blank=True, null=True)