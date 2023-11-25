from django.db import models
from course.models import Subject

class Teacher(models.Model):

    GENDER_CHOICES = [
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    ]

    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    age = models.IntegerField(max_length=3)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    job = models.CharField(max_length=30)
    education = models.CharField(max_length=100)
    experience = models.IntegerField(max_length=2)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.surname} {self.name} {self.last_name}"

    class Meta:
        ordering = ['surname', 'name', 'last_name']


