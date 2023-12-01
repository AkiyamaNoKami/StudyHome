from django.shortcuts import render
from .models import Teacher

def teacher_all(request):
    teachers = Teacher.objects.all().filter(is_active=True)
    return render(request, 'school/team.html', {'teachers': teachers})
