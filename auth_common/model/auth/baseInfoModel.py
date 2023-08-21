from django.db import models


class BaseInfoModel(models.Model):
    craeted_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
