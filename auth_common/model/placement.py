# from .student import StudentProfile
# from .internship import Internship
# from django.db import models


# class Placement(models.Model):
#     placement_id = models.AutoField(primary_key=True)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     supervisor = models.CharField(max_length=255)
#     student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
#     internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
#     STATUS_CHOICES = [
#         ("ongoing", "Ongoing"),
#         ("completed", "Completed"),
#     ]
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ongoing")
