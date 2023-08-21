from django.db import models
from .organization import OrganizationProfile
from .auth import CustomUserModel


class StudentProfile(CustomUserModel):
    student_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15)
    university = models.CharField(max_length=255)
    skills = models.TextField()
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    company = models.ForeignKey(
        OrganizationProfile, on_delete=models.SET_NULL, null=True, blank=True
    )
