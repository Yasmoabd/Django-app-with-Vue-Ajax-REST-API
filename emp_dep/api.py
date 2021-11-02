from django.http import JsonResponse
import json
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Employee, Department


def addEmployee_api(request):
    if request.method == "POST":
        print("TRUE")
        data = json.load(request)
        e = Employee(name=data.get('name'),join_date=timezone.now(),age=data.get('age'))
        e.save()
        return JsonResponse({})


def employees_api(request):
    '''
        API entry point for list of countries
        On POST: Create a new countries
    '''
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
    return JsonResponse({
        'departments': [
            department.to_dict()
            for department in Department.objects.all()
        ]
    })