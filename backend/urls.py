from django.urls import path
from backend import views

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'categories', views.getAllCategories, name="get_categories"),
    path(r'courses', views.getAllCourses, name="get_courses"),
]
