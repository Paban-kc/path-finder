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
    # JOB_TYPE_CHOICES = [
    #     ("full_time", "full_time"),
    #     ("part_time", "part_time"),
    #     ("contract", "contract"),
    #     ("temporary", "temporary"),
    #     ("volunteer", "volunteer"),
    # ]
    # job_type = models.CharField(max_length=20,choices=JOB_TYPE_CHOICES)
    # EXPERIENCE_LEVEL_CHOICES=[
    #     ("internship","internship"),
    #     ("entry_level","entry_level"),
    #     ("associate","associate"),
    #     ("mid_senior_level","mid_senior_level"),
    #     ("director","director"),
    # ]
    # experience_level=models.CharField(max_length=20,choices=EXPERIENCE_LEVEL_CHOICES)

    location=models.CharField(max_length=20)

    STATUS_CHOICES = [
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ongoing")
