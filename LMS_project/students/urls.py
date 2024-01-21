from django.urls import path
from views import (
    StudentListCreateView, StudentRetrieveUpdateDestroyView,
    EnrollmentListCreateView, EnrollmentRetrieveUpdateDestroyView,
)
from course.views import CourseViewSet


urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-retrieve-update-destroy'),
    path('courses/', CourseViewSet.as_view(), name='course-list-create'),
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', EnrollmentRetrieveUpdateDestroyView.as_view(), name='enrollment-retrieve-update-destroy'),
]