from django.urls import include, path
from . import views
from teacher.views import teacher_all

app_name='team'

urlpatterns = [
    path('', teacher_all, name='teacher_all'),

]
