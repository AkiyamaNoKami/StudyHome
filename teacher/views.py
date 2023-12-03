from django.shortcuts import render
from .models import Teacher

def team(request):
    teachers = Teacher.objects.all().filter(is_active=True)
    return render(request, 'team/team.html', {'teachers': teachers})
