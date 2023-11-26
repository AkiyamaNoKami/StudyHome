from django.contrib import admin

from .models import Subject, Course, CourseType, Lesson, Mark

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(CourseType)
admin.site.register(Lesson)
admin.site.register(Mark)