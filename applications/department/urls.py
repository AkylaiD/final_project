from django.urls import path

from applications.department.views import DepartmentListView

urlpatterns = [
    path('departments-list/', DepartmentListView.as_view()),


]