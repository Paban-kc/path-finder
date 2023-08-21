from django.db import models
from .auth import User, CustomUserModel


class OrganizationProfile(CustomUserModel):
    company_id = models.AutoField(primary_key=True)
    industry = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField()
    contact_person = models.CharField(max_length=255)
    documents = models.FileField(upload_to="company_documents")
