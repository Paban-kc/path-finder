# Generated by Django 4.2.5 on 2023-11-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_common", "0014_remove_vacancy_is_featured"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vacancy",
            name="negotiable",
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="description",
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="requirements",
            field=models.CharField(),
        ),
    ]