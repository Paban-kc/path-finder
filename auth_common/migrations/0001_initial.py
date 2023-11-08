# Generated by Django 4.2.5 on 2023-10-31 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "male"), ("F", "female"), ("O", "other")],
                        max_length=20,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email"
                    ),
                ),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("is_student", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("craeted_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("organization_name", models.CharField(max_length=50)),
                ("industry", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("website", models.URLField()),
                ("phone_no", models.CharField(max_length=10)),
                ("alt_phone_no", models.CharField(max_length=10)),
                ("contact_person", models.CharField(max_length=255)),
                (
                    "organization_documents",
                    models.FileField(upload_to="organization_documents"),
                ),
                ("pan_no", models.BigIntegerField(blank=True, null=True)),
                ("vat_no", models.BigIntegerField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="VacancyField",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("salary", models.CharField(blank=True, max_length=5)),
                ("description", models.CharField(max_length=500)),
                ("start_date", models.DateField(auto_now=True)),
                ("end_date", models.DateField()),
                ("location", models.CharField(max_length=255)),
                ("compensation", models.CharField(max_length=255)),
                ("requirements", models.CharField(max_length=500)),
                ("application_deadline", models.DateField()),
                ("responsibilities", models.CharField(max_length=500)),
                ("qualifications", models.CharField(max_length=500)),
                ("benefits", models.CharField(max_length=500)),
                ("contact_email", models.EmailField(max_length=254)),
                ("contact_phone", models.CharField(max_length=20)),
                ("is_featured", models.BooleanField(default=False)),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("full_time", "full_time"),
                            ("part_time", "part_time"),
                            ("contract", "contract"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "experience_level",
                    models.CharField(
                        choices=[
                            ("vacancy", "vacancy"),
                            ("entry_level", "entry_level"),
                            ("associate", "associate"),
                            ("mid_senior_level", "mid_senior_level"),
                            ("director", "director"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vacancies",
                        to="auth_common.organization",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("phone_no", models.CharField(max_length=10)),
                ("alt_phone", models.CharField(max_length=10)),
                ("university", models.CharField(max_length=255)),
                ("skills", models.TextField()),
                ("photo", models.ImageField(upload_to="")),
                (
                    "resume",
                    models.FileField(blank=True, null=True, upload_to="resumes/"),
                ),
                (
                    "cover_letter",
                    models.FileField(blank=True, null=True, upload_to="resumes/"),
                ),
                ("git_hub", models.URLField()),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_common.organization",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Placement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("supervisor", models.CharField(max_length=255)),
                ("supervisor_phone_no", models.CharField(blank=True, max_length=255)),
                ("location", models.CharField(max_length=20)),
                (
                    "status",
                    models.CharField(
                        choices=[("ongoing", "Ongoing"), ("completed", "Completed")],
                        default="ongoing",
                        max_length=20,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_common.organization",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_common.student",
                    ),
                ),
                (
                    "vacancy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_common.vacancy",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("rating", models.PositiveIntegerField()),
                ("comments", models.TextField()),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_common.organization",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_common.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("date_applied", models.DateField()),
                ("status", models.CharField(max_length=255)),
                ("resume", models.FileField(upload_to="applications/")),
                ("cover_letter", models.TextField()),
                ("is_approved", models.BooleanField(default=False)),
                (
                    "student_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_user",
                        to="auth_common.student",
                    ),
                ),
                (
                    "vacancy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="auth_common.vacancy",
                    ),
                ),
            ],
            options={
                "unique_together": {("student_profile", "vacancy")},
            },
        ),
    ]
