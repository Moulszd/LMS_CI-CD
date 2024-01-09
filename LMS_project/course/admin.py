from django.contrib import admin

from .models import Course
from .models import Category

admin.site.register(Course)
admin.site.register(Category)