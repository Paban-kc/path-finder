from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, is_student,gender, first_name,last_name, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email), is_student=is_student,gender=gender, first_name=first_name,last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name,gender=None,last_name=None, password=None):
        """
        Creates and saves a superuser with the given email,name date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name="",
            gender="",
            is_student=False
        
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
