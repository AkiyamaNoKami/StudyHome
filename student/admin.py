from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Student, StudentCourse

class StudentCourseInline(admin.TabularInline):
    model = StudentCourse
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'last_name', 'age', 'gender', 'parents_phone', 'parents_email', 'phone', 'email', 'description']
    inlines = [StudentCourseInline]
    filter_vertical = ['course']
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('Courses', is_stacked=False)},
    }

@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ['student', 'course']


admin.site.register(Student, StudentAdmin)
