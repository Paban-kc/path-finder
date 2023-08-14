from django.db import models


class Organization(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField()
    contact_person = models.CharField(max_length=255)
    documents = models.FileField(upload_to="company_documents")
