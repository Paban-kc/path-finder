# from auth_common.model.auth.user import User
# from auth_common.model.internShipField import InternshipField
# from .organization import OrganizationProfile
# from .auth import BaseInfoModel
# from django.db import models


# class Internship(BaseInfoModel):
#     fields = models.ManyToManyField(InternshipField)
#     internship_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     start_date = models.DateField()
#     end_date = models.DateField()
#     location = models.CharField(max_length=255)
#     compensation = models.CharField(max_length=255)
#     requirements = models.TextField()
#     company = models.ForeignKey(OrganizationProfile, on_delete=models.CASCADE)
