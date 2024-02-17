# Generated by Django 4.2.1 on 2024-02-17 08:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Interview",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.PositiveIntegerField(default=0)),
                ("publish_time", models.DateTimeField(auto_now_add=True)),
                ("feedback", models.JSONField(default=dict)),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_interviews",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "interviewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interviews",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interviews",
                        to="job.job",
                    ),
                ),
                (
                    "resume",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interviews",
                        to="job.resume",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Invitation",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.PositiveIntegerField(default=0)),
                ("message", models.CharField(max_length=200)),
                (
                    "response",
                    models.PositiveIntegerField(
                        choices=[(0, "未回复"), (1, "同意"), (2, "拒绝"), (3, "取消")], default=0
                    ),
                ),
                ("publish_time", models.DateTimeField(auto_now_add=True)),
                ("update_time", models.DateTimeField(auto_now=True)),
                (
                    "due_time",
                    models.DateTimeField(
                        default=django.db.models.expressions.CombinedExpression(
                            models.F("publish_time"),
                            "+",
                            models.Value(datetime.timedelta(days=3)),
                        )
                    ),
                ),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_invitation",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "interview",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invitations",
                        to="job.interview",
                    ),
                ),
                (
                    "interviewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interview_invitation",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
