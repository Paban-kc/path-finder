# Generated by Django 4.2.5 on 2023-11-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_common", "0011_alter_placement_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="vacancy",
            name="banner_img",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
