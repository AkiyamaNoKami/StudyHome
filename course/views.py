from django.shortcuts import render
from .models import Course

def index(requets):
    course = Course.objects.all()
    context = {'course':course}
    return render(requets, 'school/base.html', context)
