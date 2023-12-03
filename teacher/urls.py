from django.urls import include, path
from . import views
from teacher.views import team

app_name='team'

urlpatterns = [
    path('', team, name='teacher_all'),

]
