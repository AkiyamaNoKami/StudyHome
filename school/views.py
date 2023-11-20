from django.shortcuts import render

def product_all(request):
    return render(request, 'school/index.html')
