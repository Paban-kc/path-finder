from auth_common.model import internShipField
from auth_common.model.auth.user import User
from auth_common.model.organization import Organization
from .auth import BaseInfoModel
from django.db import models


class Internship(BaseInfoModel):
    title = models.CharField(max_length=255)
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
        Organization, on_delete=models.CASCADE, related_name="internships"
    )
