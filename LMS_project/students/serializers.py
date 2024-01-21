from rest_framework import serializers
from models import Student, Enrollment
from course.serializer import CourseSerializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id","first_name","last_name","email","date_of_birth","phone_number"]

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        student = StudentSerializer()
        course = CourseSerializer()

