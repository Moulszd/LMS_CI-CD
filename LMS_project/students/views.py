
# Create your views here.

from rest_framework import viewsets
from models import Student, Enrollment
from serializers import StudentSerializer, EnrollmentSerializer

class StudentListCreateView(viewsets.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyView(viewsets.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentListCreateView(viewsets.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentRetrieveUpdateDestroyView(viewsets.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer