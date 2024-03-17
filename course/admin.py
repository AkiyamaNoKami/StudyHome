from django.contrib import admin

from .models import Subject, Course, CourseType, Lesson, Mark, Homework, StudentHomework
from teacher.admin import TeacherCourseInline
from student.admin import StudentCourseInline

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'subject', 'duration', 'cost', 'description']
    inlines = [TeacherCourseInline, StudentCourseInline]

    def get_teachers(self, obj):
        return ", ".join([str(teacher) for teacher in obj.teacher.all()])

    def get_students(self, obj):
        return ", ".join([str(student) for student in obj.students.all()])

    get_teachers.short_description = 'Teachers'
    get_students.short_description = 'Students'
    readonly_fields = ['get_teachers', 'get_students']


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'student', 'score']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'student':
            lesson_id = request.resolver_match.kwargs.get('object_id')
            if lesson_id:
                kwargs['queryset'] = Mark.objects.filter(lesson_id=lesson_id).values('student')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CourseType)
class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ['type']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'course', 'teacher', 'date', 'duration', 'video_link']


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'task_1', 'task_2', 'task_3', 'task_4', 'answer_1', 'answer_2', 'answer_3', 'answer_4']


@admin.register(StudentHomework)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['student', 'homework', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'total_grade', 'watch_lesson']