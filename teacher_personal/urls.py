from django.urls import include, path
from .views import teacher_personal_view, teacher_homework_view, update_grade_view, journal_view, teacher_students_view, teacher_salary_view
from django.contrib.auth.views import LogoutView

app_name='teacher_personal'

urlpatterns = [
    path('', teacher_personal_view, name='teacher_personal'),
    path('homeworks/<int:lesson_id>/', teacher_homework_view, name='teacher_homeworks'),
    path('update_grade/<int:lesson_id>/', update_grade_view,name='update_grade'),
    path('journal/', journal_view, name='teacher_journal'),
    path('teacher_students/', teacher_students_view, name='teacher_students'),
    path('teacher_salary/', teacher_salary_view, name='teacher_salary'),
    path('logout/', LogoutView.as_view(next_page='account:login'), name='logout'),
]