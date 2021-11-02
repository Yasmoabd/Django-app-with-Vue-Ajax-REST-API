from django.urls import path

from . import views
from emp_dep.api import employees_api, departments_api, employee_api

urlpatterns = [
    path('', views.index, name='index'),
    path('api/employees/', employees_api, name="employees api"),
    path('api/departments/', departments_api, name="departments api"),
    path('api/employee/<int:employee_id>/', employee_api, name="employee api"),
]