from django.db import models

# Create your models here.
class Course (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    course=models.CharField(max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name