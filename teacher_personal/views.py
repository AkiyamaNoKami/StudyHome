from django.shortcuts import render, redirect
from teacher.models import TeacherCourse
from django.shortcuts import get_object_or_404
from course.models import Lesson, Homework, StudentHomework
from account.models import Account
from django.contrib.auth.decorators import login_required

@login_required(login_url='account:login')
def teacher_personal_view(request):
    try:
        account = request.user
        if account.teacher:
            teacher = account.teacher
            lessons = Lesson.objects.filter(teacher=teacher)
            context = {'lessons': lessons}
            return render(request, 'teacher_pm/teacher_lessons.html', context)

        else:
            return redirect('account:login')
    except Account.DoesNotExist:
        return redirect('account:login')


#снести старую базу данных и создать новые записи чтобы проверить работоспособность уроков (их айди)
@login_required(login_url='account:login')
def teacher_homework_view(request, lesson_id):
    try:
        account = request.user
        if account.teacher:
            teacher = account.teacher
            # lessons = Lesson.objects.filter(lesson_id__isnull=False)
            lessons = get_object_or_404(Lesson, pk=lesson_id, teacher=teacher)
            homeworks = StudentHomework.objects.filter(homework__lesson__teacher=teacher)
            total_homework = Homework.objects.filter(lesson=lessons).first()
            context = {'homeworks': homeworks, 'total_homework': total_homework, 'lessons': lessons}
            print(context)
            print("Teacher logged in successfully!")
            return render(request, 'teacher_pm/teacher_homework.html', context)
        else:
            return redirect('account:login')

    except Account.DoesNotExist:
        return redirect('account:login')