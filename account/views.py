from django.shortcuts import render

def login(requets):
    return render(requets, 'account/login.html')

def registration(request):
    return render(request, 'account/registration.html')