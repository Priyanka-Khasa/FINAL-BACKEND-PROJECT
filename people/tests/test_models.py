import pytest
from people.models import Department, Role, Employee
from datetime import date

@pytest.mark.django_db
def test_create_employee():
    dep = Department.objects.create(name="Engineering")
    role = Role.objects.create(title="Developer")
    emp = Employee.objects.create(first_name="Priyanka", last_name="Khasa", email="priyanka@example.com",
                                  department=dep, role=role, salary=90000, date_joined=date(2024,1,1))
    assert emp.id is not None
    assert emp.department.name == "Engineering"
