from django.urls import include, path
from .views import teacher_personal_view, teacher_homework_view, update_grade_view, journal_view

app_name='teacher_personal'

urlpatterns = [
    path('', teacher_personal_view, name='teacher_personal'),
    path('homeworks/<int:lesson_id>/', teacher_homework_view, name='teacher_homeworks'),
    path('update_grade/<int:lesson_id>/', update_grade_view,name='update_grade'),
    path('journal/', journal_view, name='teacher_journal'),
]