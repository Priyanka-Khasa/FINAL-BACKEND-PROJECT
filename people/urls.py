from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, RoleViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename="department")
router.register(r'roles', RoleViewSet, basename="role")
router.register(r'employees', EmployeeViewSet, basename="employee")

urlpatterns = [
    path('', include(router.urls)),
]
