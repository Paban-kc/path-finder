# Generated by Django 4.2.3 on 2024-11-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='similarity_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]