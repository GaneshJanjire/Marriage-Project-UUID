# Generated by Django 5.1.2 on 2024-10-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile_app', '0002_userprofile_password_userprofile_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='income',
            field=models.CharField(max_length=100),
        ),
    ]
