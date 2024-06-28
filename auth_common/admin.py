# auth_common/admin.py

from django.contrib import admin
from auth_common.model.organization import Organization

from auth_common.model.vacancy import Vacancy
from .model.auth import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    # list_display = ["id", "email", "name", "is_admin", "is_student"]
    list_display = ("email", "first_name", "last_name", "is_admin")
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        (
            "Personal info",
            {"fields": ["name"]},
        ),
        (
            "Permissions",
            {"fields": ["is_admin"]},
        ),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "password",
                    "confirm_password",
                ],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(Vacancy)
admin.site.register(Organization)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
