from django.urls import include, path
from . import views
from teacher.views import teacher_all

app_name='team'

urlpatterns = [
    path('', views.teacher_all, name='team')

]
