from django.db import models

from auth_common.model.auth.user import User

from .auth import BaseInfoModel


class Organization(BaseInfoModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="organization_user"
    )
    photo=models.ImageField(blank=True,null=True)
    organization_name = models.CharField(max_length=50,blank=True,null=True)
    industry = models.CharField(max_length=255,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    website = models.URLField(blank=True,null=True)
    phone_no = models.CharField(max_length=10,blank=True,null=True)
    alt_phone_no = models.CharField(max_length=10,blank=True,null=True)
    contact_person = models.CharField(max_length=255,blank=True,null=True)
    organization_documents = models.FileField(upload_to="organization_documents",blank=True,null=True)
    pan_no = models.BigIntegerField(null=True, blank=True)
    vat_no = models.BigIntegerField(null=True, blank=True)
    is_verified=models.BooleanField(default=False)
