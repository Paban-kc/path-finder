from auth_common.model.organization import Organization
from auth_common.model.student import Student
from .vacancy import Vacancy
from django.db import models


class Placement(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    supervisor = models.CharField(max_length=255)
    supervisor_phone_no = models.CharField(max_length=255, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    location=models.CharField(max_length=20)
    status = models.CharField(max_length=20,default="Pending")
