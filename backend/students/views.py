
from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.



class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



