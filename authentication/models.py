from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fast_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    bio=models.TextField(blank=True)
    birth_date=models.DateField(null=True, blank=True)
    phone_number=models.CharField(max_length=11, blank=True)
    address=models.CharField(max_length=255, blank=True)
    profile_picture=models.ImageField(upload_to='profile/', null=True, blank=True)
    
