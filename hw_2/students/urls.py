from django.urls import path
from .views import student_list

urlpatterns = [
    path('', student_list, name='students_list'),
]
