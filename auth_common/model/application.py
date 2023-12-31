from .auth import BaseInfoModel
from auth_common.model.student import Student
from .vacancy import Vacancy

from django.db import models


class Application(BaseInfoModel):
    date_applied = models.DateField(auto_now=True)
    status = models.CharField(max_length=255,default="pending")
    student_profile = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="student_user"
    )
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name="applications"
    )
    is_approved = models.BooleanField(default=False)  

    class Meta:
        unique_together = ("student_profile", "vacancy")

        
