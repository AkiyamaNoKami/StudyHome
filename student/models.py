from django.db import models
from course.models import Course, Subject

class Student(models.Model):

    GENDER_CHOICES = [
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    ]

    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    age = models.IntegerField(max_length=3)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    parents_phone = models.CharField(max_length=100)
    parents_email = models.EmailField(max_length=100, blank=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.surname} {self.name} {self.last_name}"

    class Meta:
        ordering = ['surname', 'name', 'last_name']


