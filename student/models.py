from django.db import models


class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_promoted=True)
    
    def age_greater_than(self, age):
        return super().get_queryset().filter(age__gt=age)
    
    
class Student(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    is_promoted = models.BooleanField()
    
    promoted_students = StudentManager()

    def __str__(self):
        return f"<Student {self.name}"