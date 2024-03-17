from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


@admin.register(Account)
class TeacherCourseAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'student']
