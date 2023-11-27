from django.contrib import admin

from .models import Subject, Course, CourseType, Lesson, Mark
from teacher.admin import TeacherCourseInline
from student.admin import StudentCourseInline
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

admin.site.register(Subject)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseType)
admin.site.register(Lesson)
admin.site.register(Mark)