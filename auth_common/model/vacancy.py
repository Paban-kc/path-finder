from auth_common.model import vacancyField
from auth_common.model.auth.user import User
from auth_common.model.organization import Organization
from .auth import BaseInfoModel
from django.db import models


class Vacancy(BaseInfoModel):
    title = models.CharField(max_length=255)
    industry = models.CharField(max_length=50)
    salary = models.CharField(max_length=5, blank=True)
    duration = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    compensation = models.CharField(max_length=255)
    requirements = models.CharField(max_length=500)
    application_deadline = models.DateField()
    responsibilities = models.CharField(max_length=500)
    qualifications = models.CharField(max_length=500)
    benefits = models.CharField(max_length=500)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    is_featured = models.BooleanField(default=False)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="vacancies"
    )
    JOB_TYPE_CHOICES = [
        ("full_time", "full_time"),
        ("part_time", "part_time"),
        ("contract", "contract"),
    ]
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    EXPERIENCE_LEVEL_CHOICES = [
        ("vacancy", "vacancy"),
        ("entry_level", "entry_level"),
        ("associate", "associate"),
        ("mid_senior_level", "mid_senior_level"),
        ("director", "director"),
    ]
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES)
