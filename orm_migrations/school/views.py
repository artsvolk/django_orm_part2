from django.shortcuts import render
from .models import Student

def students_list(request):
    students = Student.objects.prefetch_related('teachers').order_by('group')
    return render(request, 'school/students_list.html', {'object_list': students})