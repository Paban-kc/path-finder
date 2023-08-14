from .student import Student
from .internship import Internship

from django.db import models


class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    date_applied = models.DateField()
    status = models.CharField(max_length=255)
    resume = models.FileField(upload_to="applications/")
    cover_letter = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
