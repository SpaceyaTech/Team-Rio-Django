# Generated by Django 4.1.3 on 2022-11-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="verification_code",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
