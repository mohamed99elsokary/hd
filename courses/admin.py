from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Courses)
admin.site.register(models.Lectures)
admin.site.register(models.exams)
admin.site.register(models.exam_solves)
admin.site.register(models.exam_grades)
admin.site.register(models.Videos)
admin.site.register(models.Questions)
admin.site.register(models.Answers)
admin.site.register(models.Files)
admin.site.register(models.Images)
