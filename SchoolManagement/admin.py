from django.contrib import admin
from .models import Student, Teacher
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'rollNo', 'phone', 'email', 'created_at', 'updated_at']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'subject', 'created_at', 'updated_at']