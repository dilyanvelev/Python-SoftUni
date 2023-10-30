from django.http import HttpResponse
from django.shortcuts import render

from employees_app.employees.models import Employee, Department


# Create your views here.


def index(request):
    employees = [employee.first_name for employee in Employee.objects.all()]
    departments = [department.name for department in Department.objects.all()]

    context = {
        'number_1': 123,
        'number_2': 321,
        'number_3': 200,
        'caps': 'SoMeThInG',
        'title': 'Employees list',
        'employees': employees,
        'departments': departments,
        'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
    return render(request, 'template_examples/index.html', context)
