# auth_common/admin.py

from django.contrib import admin
from .model.user import User
from .model.userManager import UserManager


# Register your models here.
# auth_common/admin.py


class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "is_active", "is_admin")
    list_filter = ("is_active", "is_admin")
    search_fields = ("email", "name")
    ordering = ("email",)


admin.site.register(User, UserAdmin)
