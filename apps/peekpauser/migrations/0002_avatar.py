# Generated by Django 4.2.1 on 2024-02-17 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("peekpauser", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Avatar",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("url", models.URLField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="avatar",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
