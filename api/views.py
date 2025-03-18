from django.shortcuts import render , get_object_or_404
from django.http import JsonResponse
from student.models import student
from .serializers import student_serializers , employee_serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from employees.models import employee
from rest_framework.views import APIView
from rest_framework import mixins , generics , viewsets
from blogs.models import Blog , Comment
from blogs.serializers import BlogSerializers , CommentSerializers
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET' , 'POST'])
def students_view(request):
    if request.method == "GET":
        students = student.objects.all()
        serializers = student_serializers(students , many = True)
        return Response(serializers.data , status= status.HTTP_200_OK)
    elif request.method =="POST":
        serializers = student_serializers(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status=status.HTTP_201_CREATED)
        print(serializers.errors)
        return Response(serializers.errors , status = status.HTTP_400_BAD_REQUEST)
    
    
    
    
    # Get a single object primary key based operation 
    
@api_view(['GET' , 'PUT' ,'DELETE'])
def student_detail_view(request , pk):
    try:
        students = student.objects.get(pk = pk )
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializers = student_serializers(students)
        return Response( serializers.data, status= status.HTTP_200_OK)
    elif request.method =="PUT":
        serializers =student_serializers(students , data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status = status.HTTP_200_OK)
        else:
            return Response(serializers.data , status= status.HTTP_502_BAD_GATEWAY)
        
    elif request.method =="DELETE":
        students.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
    
    
# class Employees(APIView):
#     def get(self , request):
#         employees = employee.objects.all()
#         serializers = employee_serializers(employees , many = True)
#         return Response(serializers.data , status=status.HTTP_200_OK)
    
#     def post(self , request):
#         serializers = employee_serializers(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data , status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.errors , status=status.HTTP_400_BAD_REQUEST)
        
        
# class Employeesdetail(APIView):
#     def get_object(self, pk):
#         try:
#             return employee.objects.get(pk=pk)
#         except employee.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         Employee = self.get_object(pk)
#         if Employee is None:
#             return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = employee_serializers(Employee)  # No request.data needed
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self , pk , request):
#         employee = self.get_object(pk)
#         serializers = employee_serializers(employee , data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data , status= status.HTTP_200_OK)
#         else:
#             return Response(serializers.errors , status= status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self , pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status= status.HTTP_200_OK)

# mixins
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employee_serializers

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)  # Correctly uses list mixin

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)  # Correctly uses create mixin


# mixins
# class Employeesdetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employee_serializers
#     lookup_field = "pk"  

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)  

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs) 

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)  



# using generics
# ###

# class Employees(generics.ListAPIView , generics.CreateAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employee_serializers
    


# class Employeesdetail(generics.RetrieveAPIView , generics.DestroyAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employee_serializers
#     lookup_field = "pk"
# ###    



# view set 

# class Employeeviewset(viewsets.ViewSet):
#     def list(self , request):
#         queryset = employee.objects.all()
#         serializers = employee_serializers(queryset , many = True)
#         return Response(serializers.data)
    
    
#     def create(self , request):
#         serializers = employee_serializers(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data , status= status.HTTP_200_OK)
#         else:
#             return Response(serializers._errors , status=status.HTTP_400_BAD_REQUEST)
        
        
        
#     def retrieve(self,request , pk = None):
#         Employee = get_object_or_404(employee , pk = pk)
#         serializers  = employee_serializers(Employee)
#         return Response(serializers.data , status= status.HTTP_200_OK)
    
#     def update(self , request , pk = None):
#         Employee = get_object_or_404(employee , pk = pk)
#         serializer = employee_serializers(Employee , data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status = status.HTTP_201_CREATED)
        
#         else:
#             return Response(serializer.errors , status=status.HTTP_404_NOT_FOUND)
        
        
#     def delete(self , request , pk = None):
#         Employee =  get_object_or_404(employee , pk = pk)
#         Employee.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)




# now just using model view set we  can do primary key and non- primary key operations easily

class Employeeviewset(viewsets.ModelViewSet):
    queryset =employee.objects.all()
    serializer_class = employee_serializers
    
    
    # By just three lines of code we are making standard crud operations
    
    
    
    
class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    
    



class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
   
    
    
    
    
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = "pk"
    


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    lookup_field = "pk"
    
    
    
    
    
    
    
class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 100

class MyCustomView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    pagination_class = CustomPagination 
     