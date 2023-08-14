from django.db import models


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    university = models.CharField(max_length=255)
    skills = models.TextField()
    resume = models.FileField(upload_to="resumes/")
