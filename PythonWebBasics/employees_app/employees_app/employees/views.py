from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from random import randint

from employees_app.employees.models import Department, Employee


def validate_positive(value):
    if value < 0:
        raise ValidationError("Value must be positive")


# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )
#     last_name = forms.CharField(
#         max_length=40,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )
#
#     age = forms.IntegerField(
#         widget=forms.TextInput(
#             attrs={
#
#                 'class': 'form-control'
#             }
#         ),
#         validators=(
#             validate_positive,
#         )
#     )

class EmployeeForm(forms.ModelForm):
    def clean(self):
        return super().clean()

    class Meta:
        model = Employee
        # fields = ('first_name', 'last_name')
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'egn': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

        }


class EmployeeOrderForms(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First name'),
            ('last_name', 'Last name'),
        )
    )


def create_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('home')
    else:
        employee_form = EmployeeForm()

    employee_order_form = EmployeeOrderForms(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')

    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,
    }

    return render(request, 'form.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == "POST":
        employee_form = EmployeeForm(request.POST, request.FILES, instance=employee)

        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee')
    else:
        employee_form = EmployeeForm(instance=employee)

    employee_form = EmployeeForm(instance=employee)
    context = {
        'employee': employee,
        'employee_form': employee_form,
    }
    return render(request, 'edit.html', context)


def home(request):
    # # department = Department(
    # #     name=f"This is new department : {randint(0, 100)}"
    # # )
    # # department.save()
    # context = {
    #     'employee_form': EmployeeForm(),
    #     # 'departments': Department.objects.all(),
    #     # 'employees': Employee.objects.all(),
    # }
    return render(request, 'index.html')

    # return render(request, 'index.html')

# def localhost(request):
#     return HttpResponse('This is localhost')
#
#
# def employees(request):
#     return HttpResponse('This is emplopyees')
#
#
# def department_details(request):
#     return HttpResponse('This is department')
#
#
# def list_departments(request):
#     return HttpResponse('This is departments')
#
#
# def list_employees(request):
#     pass
