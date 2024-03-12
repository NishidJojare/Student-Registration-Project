from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('student_registration/',views.student_registration,name='student_registration'),
    path('course_creation/',views.course_creation,name='course_creation'),
    path('student_registration_success/',views.student_registration_success,name='student_registration_success'),
    path('course_creation_success/',views.course_creation_success,name='course_creation_success'),
    path('course_list/',views.course_list,name='course_list'),
    path('',views.student_list,name='student_list'),
]