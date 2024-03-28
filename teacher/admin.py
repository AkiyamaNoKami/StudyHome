from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Teacher, TeacherCourse
from django.utils.html import format_html


class TeacherCourseInline(admin.TabularInline):
    model = TeacherCourse
    extra = 1


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'last_name', 'age', 'gender', 'subject', 'job', 'education', 'experience',
                    'phone', 'description', 'thumbnail_image']
    inlines = [TeacherCourseInline]
    filter_vertical = ['courses']
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('Courses', is_stacked=False)},
    }

    def thumbnail_image(self, obj):
        if obj.image:
            image_url = obj.image.url
            return format_html('<img src="{}" width="50" height="50" />'.format(image_url))
        else:
            return 'No image'

    thumbnail_image.short_description = 'Thumbnail'
    thumbnail_image.allow_tags = True


@admin.register(TeacherCourse)
class TeacherCourseAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'course']
