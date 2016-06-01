from django.contrib import admin

# Register your models here.
from .models import University, Course, Student 
admin.site.register(University) 
admin.site.register(Course) 
admin.site.register(Student)