from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import site


from Employees.Apps.mysite.models import *
# Register your models here.
admin.site.register(Employee,DescricaoAdmin)
