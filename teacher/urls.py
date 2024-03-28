from django.urls import path
from teacher.views import team

app_name = 'team'

urlpatterns = [
    path('', team, name='teacher_all'),

]
