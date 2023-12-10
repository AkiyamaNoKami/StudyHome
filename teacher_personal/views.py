from django.shortcuts import render, redirect
from teacher.models import TeacherCourse
from course.models import Lesson
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
            lessons = Lesson.objects.filter(teacher=teacher)
            context = {'lessons': lessons}
            print(lessons)
            print(context)
            print("Teacher logged in successfully!")  # Добавьте эту строку
            return render(request, 'teacher_pm/teacher_lessons.html', context)

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
