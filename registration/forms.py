from django import forms 
from registration.models import Student,Course 

class StudentForm(forms.ModelForm): 
    class Meta:
        model = Student
        fields=['full_name','email','course']
         
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course 
        fields=['name','description']