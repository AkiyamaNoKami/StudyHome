from django.shortcuts import render, redirect
from .forms import GradeForm
from django.shortcuts import get_object_or_404
from course.models import Lesson, Homework, StudentHomework
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
            lessons = Lesson.objects.filter(pk=lesson_id, teacher=teacher)
            if lessons.exists():
                lesson = lessons.first()
                homeworks = StudentHomework.objects.filter(homework__lesson=lesson)
                total_homework = Homework.objects.filter(lesson=lesson).first()
                context = {'homeworks': homeworks, 'total_homework': total_homework, 'lesson': lesson}
                return render(request, 'teacher_pm/teacher_homework.html', context)
        else:
            return redirect('account:login')

    except Account.DoesNotExist:
        return redirect('account:login')

@login_required(login_url='account:login')
def update_grade_view(request, lesson_id):
    try:
        account = request.user
        if account.teacher:
            teacher = account.teacher
            lesson = Lesson.objects.get(pk=lesson_id, teacher=teacher)

            if request.method == 'POST':
                form = GradeForm(request.POST)
                if form.is_valid():
                    homework_id = form.cleaned_data['homework_id']
                    grade = form.cleaned_data['grade']

                    # homework_id = request.POST.get('homework_id')
                    # grade = request.POST.get('grade')

                    student_homework = get_object_or_404(StudentHomework, pk=homework_id)
                    student_homework.total_grade = grade
                    student_homework.save()

                    return redirect('teacher_personal:teacher_homeworks', lesson_id=lesson_id)
                else:
                    messages.error(request, 'Пожалуйста введите корректные значения, оценка должна быть от 0 до 5')
            else:
                form = GradeForm()
            return render(request, 'teacher_pm/teacher_homework.html', {'lesson': lesson})
    except Account.DoesNotExist:
        return redirect('account:login')