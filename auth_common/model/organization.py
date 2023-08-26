from django.db import models

from auth_common.model.auth.user import User

from .auth import BaseInfoModel


class Organization(BaseInfoModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="organization_user")
    company_name=models.CharField(max_length=50)
    company_id = models.AutoField(primary_key=True)
    industry = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField()
    phone_no = models.CharField(max_length=10)
    alt_phone_no = models.CharField(max_length=10)
    contact_person = models.CharField(max_length=255)
    documents = models.FileField(upload_to="company_documents")
    pan_no = models.BigIntegerField(null=True, blank=True)
    vat_no = models.BigIntegerField(null=True, blank=True)
