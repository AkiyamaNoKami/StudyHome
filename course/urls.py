from django.urls import include, path
from . import views
from course.views import course

app_name='courses'

urlpatterns = [
    path('', course, name='courses_all'),
]