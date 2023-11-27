from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Teacher, TeacherCourse

class TeacherCourseInline(admin.TabularInline):
    model = TeacherCourse
    extra = 1

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'last_name', 'age', 'gender', 'subject', 'job', 'education', 'experience', 'phone', 'description']
    inlines = [TeacherCourseInline]
    filter_vertical = ['course']
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('Courses', is_stacked=False)},
    }

@admin.register(TeacherCourse)
class TeacherCourseAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'course']


admin.site.register(Teacher, TeacherAdmin)