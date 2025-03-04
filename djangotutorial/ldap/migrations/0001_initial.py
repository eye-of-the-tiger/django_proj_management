# Generated by Django 5.1.6 on 2025-02-14 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Domainname",
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
                ("domainname", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Ldapprovider",
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
                ("basedn", models.CharField(max_length=300)),
                ("name", models.CharField(max_length=50)),
                ("enabled", models.BooleanField(max_length=1)),
                ("username", models.CharField(max_length=50)),
                (
                    "domainname",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ldap.domainname",
                    ),
                ),
            ],
        ),
    ]
