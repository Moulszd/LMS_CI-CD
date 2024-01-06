from .models import Course, Category
from rest_framework import permissions, viewsets

from .serializers import CategroySerializer


# class CourseViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Course.objects.all().order_by('-date_joined')
#     serializer_class = CourseSerializer
#     permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = Category
    permission_classes = [permissions.IsAuthenticated]