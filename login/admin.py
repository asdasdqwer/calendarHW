from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(CheckBox)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(SubjectClass)
admin.site.register(Task)