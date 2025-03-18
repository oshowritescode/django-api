from django.urls import path , include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employees" , views.Employeeviewset , basename= "employee")

urlpatterns = [
    path('students/' , views.students_view),
    path('students/<int:pk>/', views.student_detail_view),
    # path('employees/' , views.Employees.as_view()),
    # path('employees/<int:pk>/' , views.Employeesdetail.as_view()), #this is created to put and delete commands for data so that with proper id 
    # # we can put means update and delete the data of employee
    path('' , include(router.urls)),
    path("blogs/" , views.BlogsView.as_view()),
    path("comments/" , views.CommentsView.as_view()),
    path('blogs/<int:pk>/' , views.BlogDetailView.as_view()),
    path('comments/<int:pk>/' , views.CommentDetailView.as_view()),

]
