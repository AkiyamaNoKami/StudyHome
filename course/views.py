from django.shortcuts import render
from .models import Course

def course(requets):
    course = Course.objects.all()
    context = {'course':course}
    return render(requets, 'courses/courses.html', context)
