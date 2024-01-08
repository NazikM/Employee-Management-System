from django.shortcuts import render
from .models import Employee


def employee_hierarchy(request):
    employees = Employee.objects.filter(supervisor=None)
    return render(request, 'employees/employee_hierarchy.html', {'employees': employees})


def get_next_level_employees(request, supervisor_id):
    employees = Employee.objects.filter(supervisor=supervisor_id).values('id', 'full_name', 'position', 'email')
    return render(request, 'employees/employee_tree.html', {'employees': employees})


def employee_list(request):
    employees = Employee.objects.all()

    # Sorting logic
    sort_field = request.GET.get('sort_field', 'full_name')
    employees = employees.order_by(sort_field)

    # Searching logic
    search_query = request.GET.get('search_query', '')
    if search_query:
        employees = employees.filter(full_name__icontains=search_query,
                                     position__icontains=search_query,
                                     email__icontains=search_query)

    context = {'employees': employees}
    return render(request, 'employees/employees_list.html', context)
