
from django.shortcuts import render
from rest_framework import generics

from applications.department.models import Department
from applications.department.serializers import DepartmentSerializer


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
