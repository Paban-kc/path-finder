# Generated by Django 4.2.5 on 2023-11-25 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auth_common", "0013_vacancy_negotiable_alter_vacancy_salary"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vacancy",
            name="is_featured",
        ),
    ]
