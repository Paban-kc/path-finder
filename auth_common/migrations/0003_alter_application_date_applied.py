# Generated by Django 4.2.5 on 2023-11-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_common", "0002_alter_organization_photo_alter_student_photo_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="date_applied",
            field=models.DateField(auto_now=True),
        ),
    ]
