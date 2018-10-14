from django.db import models
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django.contrib.admin import ModelAdmin
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template.context import RequestContext


class Employee(models.Model):

  name = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  email = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  department = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  objects = models.Manager()

class DescricaoAdmin(ModelAdmin):
 
  list_display = ['name', 'email', 'department'] 
