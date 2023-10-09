
from auth_common.model.organization import Organization
from auth_common.model.student import Student
from .internship import Internship
from django.db import models


class Placement(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    supervisor = models.CharField(max_length=255)
    supervisor_phone_no = models.CharField(max_length=255,blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ongoing")
