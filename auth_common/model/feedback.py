from django.db import models
from .student import Student
from .organization import Organization


class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date = models.DateField()
    rating = models.PositiveIntegerField()
    comments = models.TextField()

    def __str__(self):
        return f"Feedback from {self.student} to {self.organization} on {self.date}"