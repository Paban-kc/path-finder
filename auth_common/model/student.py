from django.db import models

from auth_common.model.auth.user import User
from .organization import Organization
from .auth import BaseInfoModel


class Student(BaseInfoModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_user")
    phone = models.CharField(max_length=10)
    alt_phone = models.CharField(max_length=10)
    university = models.CharField(max_length=255)
    skills = models.TextField()
    photo = models.ImageField()
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    cover_letter = models.FileField(upload_to="resumes/", blank=True, null=True)
    git_hub = models.URLField()
    company = models.ForeignKey(
        Organization, on_delete=models.CASCADE, null=True, blank=True
    )
