from django.shortcuts import render, redirect

def product_all(request):
    return render(request, 'school/index.html')

def about(request):
    return render(request, 'school/about.html')

def contact(request):
    return render(request, 'school/contact.html')

def courses(request):
    return render(request, 'school/courses.html')

def team(request):
    return redirect('teacher_all')

def testimonial(request):
    return render(request, 'school/testimonial.html')
