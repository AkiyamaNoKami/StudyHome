from django.shortcuts import render

def course(requets):
    return render(requets, 'courses/courses.html')
