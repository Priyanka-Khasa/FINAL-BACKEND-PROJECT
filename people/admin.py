from django.contrib import admin
from .models import Department, Role, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","email","department","role","salary","is_active")
    search_fields = ("first_name","last_name","email")
    list_filter = ("department","role","is_active")
