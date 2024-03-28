from django.urls import path
from course.views import course

app_name = 'courses'

urlpatterns = [
    path('', course, name='courses_all'),
]
