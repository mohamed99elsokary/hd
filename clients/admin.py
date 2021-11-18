from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Phone_numbers)
admin.site.register(models.Apartments)
admin.site.register(models.Survey)
admin.site.register(models.offer)
admin.site.register(models.order)
admin.site.register(models.Rooms)
admin.site.register(models.products_in_rooms)
