from django.db import models
from teacher.models import Teacher



class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class CourseType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    type = models.ForeignKey(CourseType, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50)
    duration = models.IntegerField(max_length=4)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    score = models.IntegerField(max_length=1)


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    mark = models.ForeignKey(Mark, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(editable=True)
    duration = models.IntegerField(max_length=3)

