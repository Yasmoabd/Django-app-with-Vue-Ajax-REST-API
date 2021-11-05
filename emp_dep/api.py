from django.http import JsonResponse
import json
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Employee, Department

def employee_api(request, employee_id):
    if request.method == "DELETE":
        employee = get_object_or_404(Employee, id=employee_id)
        employee.delete()
        return JsonResponse({})
    elif request.method == "PUT":
        data = json.load(request)
        employee = get_object_or_404(Employee, id=employee_id)
        employee.name=data.get('name')
        employee.age=data.get('age')
        employee.department_set.clear()
        for departmentID in data.get('departments'):
            employee.department_set.add(Department.objects.get(id=departmentID))
        employee.save()
        return JsonResponse({})

    return HttpResponseBadRequest("Invalid method")

def employees_api(request):
    '''
        API entry point for list of countries
        On POST: Create a new countries
    '''
    if request.method == "POST":
        data = json.load(request)
        e = Employee(name=data.get('name'),join_date=timezone.now(),age=data.get('age'))
        e.save()
        for departmentID in data.get('departments'):
            e.department_set.add(Department.objects.get(id=departmentID))
        e.save()
        return JsonResponse({})

    return JsonResponse({
        'employees': [
            employee.to_dict()
            for employee in Employee.objects.all()
        ]
    })

def departments_api(request):
    '''
        API entry point for list of countries
        On POST: Create a new countries
    '''
    if request.method == "POST":
        data = json.load(request)
        d = Department(name=data.get('name'),salary=data.get('salary'))
        d.save()
        for employeeID in data.get('employees'):
            d.employees.add(Employee.objects.get(id=employeeID))
        d.save()
        return JsonResponse({})

    return JsonResponse({
        'departments': [
            department.to_dict()
            for department in Department.objects.all()
        ]
    })

def department_api(request, department_id):
    if request.method == "DELETE":
        department = get_object_or_404(Department, id=department_id)
        department.delete()
        return JsonResponse({})

    return HttpResponseBadRequest("Invalid method")