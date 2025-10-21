from django.urls import path
from .views import summary, salary_chart

urlpatterns = [
    path('summary/', summary, name='summary'),
    path('salary-chart/', salary_chart, name='salary-chart'),
]
