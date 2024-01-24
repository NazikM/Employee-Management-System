from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Employee


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def employee_hierarchy(request):
    employees = Employee.objects.filter(supervisor=None)
    return render(
        request, "employees/employee_hierarchy.html", {"employees": employees}
    )


def get_next_level_employees(request, supervisor_id):
    employees = Employee.objects.filter(supervisor=supervisor_id).values(
        "id", "full_name", "position", "email"
    )
    return render(request, "employees/employee_tree.html", {"employees": employees})


def employee_list(request):
    employees = Employee.objects.all()

    # Sorting logic
    sort_field = request.GET.get("sort_field", "full_name")
    employees = employees.order_by(sort_field)

    # Searching logic
    search_query = request.GET.get("search_query", "")
    if search_query:
        employees = employees.filter(
            full_name__icontains=search_query,
            position__icontains=search_query,
            email__icontains=search_query,
        )

        # Check if it's an Ajax request
    if is_ajax(request=request):
        html_context = {
            "html": render_to_string(
                "employees/employee_list_ajax.html", {"employees": employees}, request
            )
        }
        return JsonResponse(html_context)
    context = {"employees": employees}
    return render(request, "employees/employees_list.html", context)
