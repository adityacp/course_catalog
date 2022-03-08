from unicodedata import category
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse

from backend.models import Course, Category


def index(request):
    return render(request, "base.html")


def getAllCategories(request):
    categories = list(Category.objects.values_list("name", flat=True))
    return JsonResponse({"data": categories})


def getAllCourses(request):
    values_list = [
        "name", "description", "start_date", "end_date", "estimated_workload",
        "weeks", "category__name", "instructor__first_name",
        "instructor__last_name"
    ]
    courses = list(Course.objects.values(*values_list))
    return JsonResponse({"data": courses})
