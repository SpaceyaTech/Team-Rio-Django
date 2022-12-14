# Generated by Django 4.1.3 on 2022-11-30 07:45

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_alter_user_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                help_text="Contact phone number",
                max_length=128,
                null=True,
                region=None,
            ),
        ),
    ]
