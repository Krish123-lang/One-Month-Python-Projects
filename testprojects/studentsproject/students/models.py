from django.db import models

# Create your models here.


class Student(models.Model):
    DEPARTMENT_CHOICES = [
        ("computer", "Computer Engineering"),
        ("civil", "Civil Engineering"),
        ("electronics", "Electronics Engineering"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
