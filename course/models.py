from django.db import models
from student.models import Student


class Subject(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class CourseType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Course(models.Model):
    type = models.ForeignKey(CourseType, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    students = models.ManyToManyField('student.Student', blank=True, related_name='courses_students', through='student.StudentCourse')
    teacher = models.ManyToManyField('teacher.Teacher', blank=True, related_name='course_teachers', through='teacher.TeacherCourse')

    def __str__(self):
        return self.title


#Добавить описание, чтобы к каждому уроку была информация, также реализовать домашку
class Lesson(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(editable=True)
    duration = models.IntegerField()
    video_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Mark(models.Model):
    score = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.score)


class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    task_1 = models.CharField(max_length=255)
    task_2 = models.CharField(max_length=255)
    task_3 = models.CharField(max_length=255)
    task_4 = models.CharField(max_length=255)
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)

    def __str__(self):
        return f'Homework for {self.lesson.title}'


class StudentHomework(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)
    total_grade = models.IntegerField(null=True, blank=True)
    watch_lesson = models.BooleanField(default=False)

    def __str__(self):
        return f'Homework for {self.student.name} on {self.homework.lesson.title}'
