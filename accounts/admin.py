from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.categories)
admin.site.register(models.accounts)
admin.site.register(models.Grades)
