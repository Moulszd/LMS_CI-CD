from .models import Course,Category
from rest_framework import serializers

class CategroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = 