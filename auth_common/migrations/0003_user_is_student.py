# Generated by Django 4.2.3 on 2023-08-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "auth_common",
            "0002_rename_created_at_user_craeted_at_alter_user_name_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_student",
            field=models.BooleanField(default=False),
        ),
    ]
