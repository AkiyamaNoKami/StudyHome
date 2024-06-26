from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Account


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Account.objects.get(username=username, password=password)
        if user is not None:
            print('Not none')
            login(request, user)
            return redirect('teacher_personal:teacher_personal')
        else:
            print('none')
            return render(
                request,
                'account/login.html',
                {'error': 'Invalid user'}
            )
    print('done')
    return render(request, 'account/login.html')


def registration(request):
    return render(request, 'account/registration.html')
