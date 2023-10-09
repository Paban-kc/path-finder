from .auth import BaseInfoModel
from auth_common.model.student import Student
from .internship import Internship

from django.db import models


class Application(BaseInfoModel):
    date_applied = models.DateField()
    status = models.CharField(max_length=255)
    resume = models.FileField(upload_to="applications/")
    cover_letter = models.TextField()
    student_profile = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="student_user"
    )
    internship = models.ForeignKey(
        Internship, on_delete=models.CASCADE, related_name="applications"
    )
    is_approved = models.BooleanField(default=False)  

    class Meta:
        unique_together = ("student_profile", "internship")
