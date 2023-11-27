from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'last_name', 'age', 'gender', 'parents_phone', 'parents_email', 'phone', 'email', 'description']
    filter_vertical = ['course',]
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('Course', is_stacked=False)},
    }


admin.site.register(Student)
