from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from emp_dep.models import Employee, Department


def index(request):
    employees = Employee.objects.all()
    request.session['last_visit'] = str(timezone.now())
    return render(request, 'emp_dep/emp&deps.html', {
        'title': "My Employees and Departments",
        'employees': employees,
        'user': request.user,
    })
