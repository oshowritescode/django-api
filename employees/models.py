from django.db import models

# Create your models here.
class employee(models.Model):
    emp_name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=200)
    designation= models.CharField(max_length= 200)
    
    
    def __str__(self):
        return self.emp_name
    