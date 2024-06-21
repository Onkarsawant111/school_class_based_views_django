# admin.py
from django.contrib import admin
from .models import Students

class Student_info(admin.ModelAdmin):
    list_display = ('name', 'age')

admin.site.register(Students, Student_info)
