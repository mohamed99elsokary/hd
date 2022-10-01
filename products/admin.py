from django.contrib import admin
import django.contrib.admin.options as admin_opt
from .models import *


def dup_event(modeladmin: admin_opt.ModelAdmin, request, queryset):
    for object in queryset:
        from_id = object.id
        object.id = None
        object.save()
        message = f"dup from {from_id} to {object.id}"
        modeladmin.log_addition(request=request, object=object, message=message)


dup_event.short_description = "Duplicate "


class MyObjAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = ["id"]
    actions = [dup_event]


admin.site.register(Products, MyObjAdmin)
admin.site.register(Questions)
admin.site.register(Categories)
admin.site.register(Tools)
