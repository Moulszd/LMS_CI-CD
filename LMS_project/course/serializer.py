from .models import Category,Course
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","category_name"] 

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id","title","description","course_category","duration_hours","duration","description","price"]
