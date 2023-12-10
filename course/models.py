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

    class Meta:
        ordering = ['title']



#Добавить описание, чтобы к каждому уроку была информация, также реализовать домашку
class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(editable=True)
    duration = models.IntegerField()
    video_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Mark(models.Model):
    score = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.score)

    class Meta:
        ordering = ['score']


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
    grade_1 = models.IntegerField(null=True, blank=True)
    grade_2 = models.IntegerField(null=True, blank=True)
    grade_3 = models.IntegerField(null=True, blank=True)
    grade_4 = models.IntegerField(null=True, blank=True)
    total_grade = models.IntegerField(null=True, blank=True)

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

    def __str__(self):
        return f'Homework for {self.student.name} on {self.homework.lesson.title}'

    def save(self, *args, **kwargs):
        self.calculate_grades()
        super().save(*args, **kwargs)

    def calculate_grades(self):
        self.grade_1 = self.calculate_single_grade(self.answer_1, self.homework.answer_1)
        self.grade_2 = self.calculate_single_grade(self.answer_2, self.homework.answer_2)
        self.grade_3 = self.calculate_single_grade(self.answer_3, self.homework.answer_3)
        self.grade_4 = self.calculate_single_grade(self.answer_4, self.homework.answer_4)

        grades = [self.grade_1, self.grade_2, self.grade_3, self.grade_4]
        valid_grades = [grade for grade in grades if grade is not None]
        total_grade = sum(valid_grades) / len(valid_grades) if valid_grades else 0
        self.total_grade = total_grade

    def calculate_single_grade(self, user_answer, correct_answer):
        return 1 if user_answer == correct_answer else 0
