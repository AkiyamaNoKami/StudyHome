from django.db import models
from student.models import Student



class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class CourseType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['type']


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    type = models.ForeignKey(CourseType, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    students = models.ManyToManyField('student.Student', blank=True, null=True, related_name='courses_students')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(editable=True)
    duration = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.score

    class Meta:
        ordering = ['score']





