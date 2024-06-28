from django.db import models

from auth_common.model.auth.user import User
from .organization import Organization
from .auth import BaseInfoModel


class Student(BaseInfoModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student_user"
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    alt_phone = models.CharField(max_length=10, blank=True, null=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    photo = models.FileField(upload_to='student_photos/',blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    cover_letter = models.FileField(upload_to="resumes/", blank=True, null=True)
    git_hub = models.URLField(blank=True, null=True)
    company = models.ForeignKey(
        Organization, on_delete=models.CASCADE, null=True, blank=True
    )
