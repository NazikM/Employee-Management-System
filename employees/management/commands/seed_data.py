import os
from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Employee
from random import randint

fake = Faker()


class Command(BaseCommand):
    help = "Seed the database with random employee data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Seeding the database..."))

        Employee.objects.all().delete()  # Clear the existing data

        self.create_employee_hierarchy()

        self.stdout.write(self.style.SUCCESS("Database seeding completed."))

    def generate_fake_employee(self):
        return {
            "full_name": fake.name(),
            "position": fake.job(),
            "hire_date": fake.date_between(start_date="-5y", end_date="today"),
            "email": fake.email(),
        }

    def create_employee_hierarchy(
        self, parent=None, depth=0, max_depth=7, max_children=5
    ):
        if depth > max_depth:
            return

        num_children = randint(1, max_children)

        for _ in range(num_children):
            fake_employee_data = self.generate_fake_employee()
            employee = Employee.objects.create(
                full_name=fake_employee_data["full_name"],
                position=fake_employee_data["position"],
                hire_date=fake_employee_data["hire_date"],
                email=fake_employee_data["email"],
                supervisor=parent,
            )

            self.create_employee_hierarchy(
                parent=employee,
                depth=depth + 1,
                max_depth=max_depth,
                max_children=max_children + 1,
            )

        if depth == max_depth:
            print(123)
