from django.shortcuts import render ,HttpResponse

# Create your views here.
def student(request):
    students = [
        {"id" : 1 , "name" :"osho" , "roll_no" : "22bee080"}   
        ]
    return HttpResponse(students)
# the above view is for web application end points
