from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name