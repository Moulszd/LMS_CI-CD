from django.urls import include, path
from rest_framework import routers

from course import views


router = routers.DefaultRouter()
# router.register(r'course', views.CourseViewSet)
router.register(r'category', views.CategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls