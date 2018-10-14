from Employees.Apps.mysite.models import Employee
from Employees.Apps.mysite.serializers import EmployeeSerializer

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

