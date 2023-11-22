from django.shortcuts import render

def product_all(request):
    return render(request, 'school/index.html')

def about(request):
    return render(request, 'school/about.html')

def contact(request):
    return render(request, 'school/contact.html')

def courses(request):
    return render(request, 'school/courses.html')

def team(request):
    return render(request, 'school/team.html')

def testimonial(request):
    return render(request, 'school/testimonial.html')
