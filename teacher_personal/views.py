from django.shortcuts import render, redirect
from course.models import Course
from account.models import Account
from django.contrib.auth.decorators import login_required

@login_required(login_url='account:login')
def teacher_personal_view(request):
    try:
        # Пытаемся получить объект аккаунта пользователя
        account = request.user
        print('account')
        # Проверяем, является ли аккаунт учителем
        if account.teacher:
            teacher = account.teacher
            courses = Course.objects.all()
            print("Teacher logged in successfully!")  # Добавьте эту строку
            return render(request, 'teacher_pm/teacher_base.html', {'courses': courses, 'teacher': teacher})

        else:
            # Если не является учителем, перенаправляем на URL приложения account
            return redirect('account:login')

    except Account.DoesNotExist:
        # Если аккаунт не существует, перенаправляем на URL приложения account
        return redirect('account:login')
    except Exception as e:
        # Логируйте ошибку, чтобы понять, что происходит
        print(e)
        return redirect('account:login')
