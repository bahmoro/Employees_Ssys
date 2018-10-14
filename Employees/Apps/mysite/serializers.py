from Employees.Apps.mysite.models import Employee
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer



class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','name', 'email', 'department')
       
        