# Generated by Django 4.2.3 on 2023-08-03 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0003_remove_course_code_remove_course_origin_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseInfo",
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
                (
                    "code",
                    models.CharField(
                        blank=True, db_column="CODE", max_length=10, null=True
                    ),
                ),
                (
                    "course_name",
                    models.CharField(
                        blank=True, db_column="COURSE_NAME", max_length=100, null=True
                    ),
                ),
                ("cu", models.IntegerField(blank=True, db_column="CU", null=True)),
                ("lh", models.IntegerField(blank=True, db_column="LH", null=True)),
                ("ph", models.IntegerField(blank=True, db_column="PH", null=True)),
                ("th", models.IntegerField(blank=True, db_column="TH", null=True)),
                ("ch", models.IntegerField(blank=True, db_column="CH", null=True)),
                (
                    "type",
                    models.CharField(
                        blank=True, db_column="Type", max_length=20, null=True
                    ),
                ),
                (
                    "remark",
                    models.CharField(
                        blank=True, db_column="Remark", max_length=50, null=True
                    ),
                ),
                (
                    "origin",
                    models.CharField(
                        blank=True, db_column="Origin", max_length=50, null=True
                    ),
                ),
                (
                    "program",
                    models.CharField(
                        blank=True, db_column="Program", max_length=50, null=True
                    ),
                ),
                ("year_of_study", models.IntegerField(blank=True, null=True)),
                ("semester", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "db_table": "course_info",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="Course",
        ),
    ]
