from django.contrib import admin
from ABC.models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','mobileno']