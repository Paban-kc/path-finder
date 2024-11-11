from auth_common.model import vacancyField
from auth_common.model.auth.user import User
from auth_common.model.organization import Organization
from .auth import BaseInfoModel
from django.db import models


class Vacancy(BaseInfoModel):
    salary = models.CharField(max_length=225, blank=True)
    duration = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    start_date = models.DateField(auto_now=True)
    location = models.CharField(max_length=255)
    requirements = models.CharField(max_length=2000)
    application_deadline = models.DateField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="vacancies"
    )
    banner_img=models.FileField(blank=True, null=True)
    similarity_score=models.DecimalField(decimal_places=2,default=0.00,max_digits=5)
    job_type = models.CharField(max_length=20)
