from django.urls import path

from employees.views import employee_hierarchy, get_next_level_employees, employee_list

urlpatterns = [
    path("", employee_hierarchy, name="employee_hierarchy"),
    path(
        "get_next_level/<int:supervisor_id>/",
        get_next_level_employees,
        name="get_next_level",
    ),
    path("employee_list/", employee_list, name="employee_list"),
]
