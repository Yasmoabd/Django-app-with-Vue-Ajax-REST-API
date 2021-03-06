from django.db import models
from django.urls import reverse

class Employee(models.Model):
    name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date joined')
    age = models.IntegerField()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'join_date': self.join_date,
            'age': self.age,
            'departments': [str(d) for d in self.department_set.all()],
            'api': reverse('employee api', kwargs={'employee_id': self.id}),
        }
    
    def __str__(self):
        return f"{self.name}"


class Department(models.Model):
    employees = models.ManyToManyField(Employee)
    name = models.CharField(max_length=200)
    salary = models.IntegerField()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'employees':[str(e) for e in self.employees.all()],
            'api': reverse('department api', kwargs={'department_id': self.id}),
        }

    def __str__(self):
        return f"{self.name}"