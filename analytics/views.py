from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from people.models import Employee, Department
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def summary(request):
    total_employees = Employee.objects.count()
    active = Employee.objects.filter(is_active=True).count()
    by_dept = list(Department.objects.values_list('name', flat=True))
    return Response({
        "total_employees": total_employees,
        "active_employees": active,
        "departments": by_dept
    })

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def salary_chart(request):
    # Avg salary per department bar chart (PNG base64)
    qs = (Employee.objects
          .values('department__name')
          .order_by('department__name'))
    data = {}
    for row in qs:
        # We'll compute per department averages
        pass
    # Better: compute with aggregation
    from django.db.models import Avg
    agg = Employee.objects.values('department__name').annotate(avg_salary=Avg('salary')).order_by('department__name')
    labels = [a['department__name'] for a in agg]
    values = [float(a['avg_salary'] or 0) for a in agg]
    plt.figure()
    plt.bar(labels, values)
    plt.xticks(rotation=45, ha='right')
    plt.title('Average Salary by Department')
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode('utf-8')
    return Response({"image_base64_png": b64})
