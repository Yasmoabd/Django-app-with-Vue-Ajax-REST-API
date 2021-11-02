from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404

from .models import Employee, Department

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