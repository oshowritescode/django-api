from rest_framework import serializers
from student.models import student
from employees.models import employee



class student_serializers(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"
        
        
        
class employee_serializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = "__all__"