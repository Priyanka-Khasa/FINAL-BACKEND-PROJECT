import pytest
from django.urls import reverse
from people.models import Department, Role, Employee
from datetime import date

@pytest.mark.django_db
def test_public_list_departments(client):
    Department.objects.create(name="Engineering")
    resp = client.get("/api/people/departments/")
    assert resp.status_code == 200
    assert resp.json()['results'][0]['name'] == "Engineering"

@pytest.mark.django_db
def test_create_requires_auth(client):
    resp = client.post("/api/people/departments/", {"name": "X"})
    assert resp.status_code in (401, 403)
