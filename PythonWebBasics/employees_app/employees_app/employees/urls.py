from django.urls import path

from employees_app.employees.views import home, create_employee, edit_employee

urlpatterns = (
    path('', home, name='home'),
    # path('employees/', employees, name='employees'),
    path('forms/', create_employee, name='create employee'),
    # path('create/', ,name='create employee'),
    path('edit/<int:pk>', edit_employee, name='edit employee'),

)
