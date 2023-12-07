from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    teacher = models.OneToOneField('teacher.Teacher', on_delete=models.CASCADE, null=True, blank=True)
    student = models.OneToOneField('student.Student', on_delete=models.CASCADE, null=True, blank=True)

