from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from .userManager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ("M", "male"),
        ("F", "female"),
        ("O", "other"),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    craeted_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    objects = UserManager()
