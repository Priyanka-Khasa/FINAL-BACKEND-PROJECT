from rest_framework import serializers
from .models import Department, Role, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField(source="department.name")
    role_title = serializers.ReadOnlyField(source="role.title")
    class Meta:
        model = Employee
        fields = ["id","first_name","last_name","email","department","role","department_name","role_title","salary","date_joined","is_active","created_at","updated_at"]
