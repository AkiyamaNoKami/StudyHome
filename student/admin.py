from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Student, StudentCourse
from django.utils.html import format_html

class StudentCourseInline(admin.TabularInline):
    model = StudentCourse
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'last_name', 'age', 'gender', 'parents_phone', 'parents_email', 'phone', 'email', 'description', 'thumbnail_image']
    inlines = [StudentCourseInline]
    filter_vertical = ['course']
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('Courses', is_stacked=False)},
    }

    def thumbnail_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        else:
            return 'No image'

    thumbnail_image.short_description = 'Thumbnail'
    thumbnail_image.allow_tags = True

@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ['student', 'course']


admin.site.register(Student, StudentAdmin)
