from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    instructor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    estimated_workload = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    weeks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        days = (self.end_date - self.start_date).days
        self.weeks = days // 7
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
